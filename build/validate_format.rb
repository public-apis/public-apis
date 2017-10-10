#!/usr/bin/env ruby

auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']

INDEX_TITLE = 1
INDEX_DESCRIPTION = 2
INDEX_AUTH = 3
INDEX_HTTPS = 4
INDEX_LINK = 5
filename = ARGV[0]
$errors = []

def add_error(line_num, val_index, message)
    case val_index
    when INDEX_TITLE
        segment = "Title"
    when INDEX_DESCRIPTION
        segment = "Description"
    when INDEX_AUTH
        segment = "Auth"
    when INDEX_HTTPS
        segment = "HTTPS"
    when INDEX_LINK
        segment = "Link"
    end
    $errors.push("(L%03d) %-14.14s #{message}" % [line_num, segment])
end

################### CHECK ALPHABETICAL ORDER ###################
section = ''
sections = []
section_to_line_num = {}
section_to_entries = Hash.new {|h,k| h[k] = Array.new }
File.foreach(filename).with_index do | line, line_num |
	if line.start_with?('###')
		section = line.sub('###', '').lstrip.chop
		sections.push(section)
		section_to_line_num[section] = line_num + 1
	end
	# Skip non-markdown table lines and table schema lines
    if !line.start_with?('|') || line.eql?("|---|---|---|---|---|\n")
        next
    end
    # char to check is the first column
    check_char = line.split("|")[1].strip.upcase
    section_to_entries[section].push(check_char)
end
sections.each do | sect |
	if section_to_entries[sect] != section_to_entries[sect].sort
		add_error(section_to_line_num[sect], INDEX_TITLE, "#{sect} section is not in alphabetical order")
	end
end

#################### CHECK LINE ENTRIES ########################
File.foreach(filename).with_index do | line, line_num |
    line_num += 1
        
    # Skip non-markdown table lines and table schema lines
    if !line.start_with?('|') || line.eql?("|---|---|---|---|---|\n")
        next
    end

    values = line.split("|")

    ################### GLOBAL ###################
    values.each.with_index do |val, val_index|
        msg = ""
        case val_index
        when INDEX_TITLE..INDEX_LINK
            # every line segment should start and end with exactly 1 space
            if val[/\A */].size != 1 || val[/ *\z/].size != 1
                add_error(line_num, val_index, "string should start and end with exactly 1 space")
            end
        end
    end
    ################# DESCRIPTION ################
    # First character should be capitalized
    desc_val = values[INDEX_DESCRIPTION].lstrip.chop
    if !/[[:upper:]]/.match(desc_val[0])
        add_error(line_num, INDEX_DESCRIPTION, "first char not uppercase")
    end
    # value should not be punctuated
    last_char = desc_val[desc_val.length-1]
    if punctuation.include?(last_char)
        add_error(line_num, INDEX_DESCRIPTION, "description should not end with \"#{last_char}\"")
    end
    #################### AUTH ####################
    # Values should conform to valid options only
    auth_val = values[INDEX_AUTH].lstrip.chop.tr('``', '')
    if !auth_keys.include?(auth_val)
        add_error(line_num, INDEX_AUTH, "not a valid option: #{auth_val}")
    end
    #################### HTTPS ###################
    # Values should be either "Yes" or "No"
    https_val = values[INDEX_HTTPS].lstrip.chop
    if !https_keys.include?(https_val)
        add_error(line_num, INDEX_HTTPS, "must use \"Yes\" or \"No\": #{https_val}")
    end
    #################### LINK ####################
    # Url should be wrapped in "[Go!]" view
    link_val = values[INDEX_LINK].lstrip.chop
    if !link_val.start_with?("[Go!](") || !link_val.end_with?(')')
        add_error(line_num, INDEX_LINK, "format should be \"[Go!](<LINK>)\": #{link_val}")
    end
end
$errors.each do | e |
    puts e
end
exit($errors.length)
