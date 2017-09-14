#!/usr/bin/env ruby
require 'httparty'
require 'ruby-progressbar'
require 'uri'
allowed_codes = [200, 302, 403, 429]
allowed_links = ["https://www.yelp.com/developers/documentation/v3"]
args = ARGV
filename = args[0]
contents = File.open(filename, 'rb') { |f| f.read }
raw_links = URI.extract(contents, ['http', 'https'])
# Remove trailing ')' from entry URLs
links = []
raw_links.each do |link|
    if link.end_with?(')')
        links.push(link[0...-1])
    else
        links.push(link)
    end
end
if links.length <= 0
    puts "no links to check"
    exit(0)
end
fails = []
# Fail on any duplicate elements
dup = links.select{|element| links.count(element) > 1}
if dup.uniq.length > 0
    dup.uniq.each do |e|
        fails.push("(DUP): #{e}")
    end
end
# Remove any duplicates from array
links = links.uniq
count = 0
total = links.length
progressbar = ProgressBar.create(:total => total,
    :format => "%a %P% | Processed: %c from %C")
# GET each link and check for valid response code from allowed_codes
links.each do |link|
    begin
        count += 1
        if allowed_links.include?(link)
            next
        end
        res = HTTParty.get(link, timeout: 10)
        if res.code.nil?
            fails.push("(NIL): #{link}")
            next
        end
        if !allowed_codes.include?(res.code)
            fails.push("(#{res.code}): #{link}")
        end
    rescue HTTParty::RedirectionTooDeep
        fails.push("(RTD): #{link}")
    rescue Net::ReadTimeout
        fails.push("(TMO): #{link}")
    rescue Net::OpenTimeout
        fails.push("(TMO): #{link}")
    rescue OpenSSL::SSL::SSLError
        fails.push("(SSL): #{link}")
    rescue SocketError
        fails.push("(SOK): #{link}")
    rescue Errno::ECONNREFUSED
        fails.push("(CON): #{link}")
    rescue Errno::ECONNRESET
        next
    end
    progressbar.increment
end
puts "#{count}/#{total} links checked"
if fails.length <= 0
    puts "all links valid"
    exit(0)
else
    puts "-- RESULTS --"
    fails.sort!
    fails.each do |e|
        puts e
    end
    exit(1)
end
