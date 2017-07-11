#!/usr/bin/env ruby
require 'faraday'
require 'uri'
allowed_codes = [200, 302, 403]
args = ARGV
filename = args[0]
fail_flag = false
contents = File.open(filename, 'rb') { |f| f.read }
links = URI.extract(contents, ['http', 'https'])
dup = links.select{|element| links.count(element) > 1 }
if dup.uniq.length > 0
    dup.uniq.each do |link|
        if link.end_with?(')')
            puts link[0...-1]
        end
    end
    exit(1)
end
links.each do |link|
    if link.end_with?(')')
        link = link[0...-1]
    end
    res = Faraday.get(link)
    if !allowed_codes.include?(res.status)
        puts "(#{res.status}): #{link}"
        fail_flag = true
    end
end
if fail_flag
    exit(1)
else
    exit(0)
end
