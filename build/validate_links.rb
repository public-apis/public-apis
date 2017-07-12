#!/usr/bin/env ruby
require 'httparty'
require 'uri'
allowed_codes = [200, 302, 403]
args = ARGV
filename = args[0]
fail_flag = false
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
fails = []
# Fail on any duplicate elements
dup = links.select{|element| links.count(element) > 1}
if dup.uniq.length > 0
    dup.uniq.each do |e|
        fails.push("Duplicate link: #{e}")
    end
    fail_flag = true
end
# Remove any duplicates from array
links = links.uniq
count = 0
total = links.length
# GET each link and check for valid response code from allowed_codes
links.each do |link|
    begin
        count += 1
        puts "(#{count}/#{total}) #{link}"
        res = HTTParty.get(link, timeout: 10)
        if !allowed_codes.include?(res.code)
            fails.push("(#{res.code}): #{link}")
            fail_flag = true
        else
            puts "\t(#{res.code})"
        end
    rescue
        puts "FAIL: (#{res.code}) #{link}"
        fails.push("(#{res.code}): #{link}")
        fail_flag = true
    end
end
if fails.length <= 0
    puts "all links valid"
else
    puts "-- RESULTS --"
end
fails.each do |e|
    puts e
end
if fail_flag
    exit(1)
else
    exit(0)
end
