#!/usr/bin/env ruby

auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']
args = ARGV
filename = args[0]
$errors = []

def add_error(line_num, val_index, message)
    case val_index
    when 1
        segment = "Title"
    when 2
        segment = "Description"
    when 3
        segment = "Auth"
    when 4
        segment = "HTTPS"
    when 5
        segment = "Link"
    end

    $errors.push("(L%03d) (#{segment}) #{message}" % line_num)
end

File.foreach(filename).with_index do | line, line_num |
    line_num += 1
    if line.start_with?('|')
        # Skip table schema lines
        if line.eql? "|---|---|---|---|---|\n"
            next
        end

        values = line.split("|")

        values.each.with_index do |val, val_index|
            msg = ""
            case val_index
            when 1..5
                if val[0] != " " || val[val.length-1] != " "
                add_error(line_num, val_index, "spacing is invalid (pad before and after string)")
                end
            end
        end

        ################# DESCRIPTION ################
        # First character should be capitalized
        desc_val = values[2].lstrip.chop
        if !/[[:upper:]]/.match(desc_val[0])
            add_error(line_num, 2, "first char not uppercase")
        end
        # value should not be punctuated
        last_char = desc_val[desc_val.length-1]
        if punctuation.include?(last_char)
            add_error(line_num, 2, "description should not end with \"#{last_char}\"")
        end
        #################### AUTH ####################
        # Values should conform to valid options only
        auth_val = values[3].lstrip.chop.tr('``', '')
        if !auth_keys.include?(auth_val)
            add_error(line_num, 3, "not a valid option: #{auth_val}")
        end
        #################### HTTPS ###################
        # Values should be either "Yes" or "No"
        https_val = values[4].lstrip.chop
        if !https_keys.include?(https_val)
            add_error(line_num, 4, "must use \"Yes\" or \"No\": #{https_val}")
        end
        #################### LINK ####################
        # Url should be wrapped in "[Go!]" view
        link_val = values[5].lstrip.chop
        if !link_val.start_with?("[Go!](") || !link_val.end_with?(')')
            add_error(line_num, 5, "format should be \"[Go!](<LINK>)\": #{link_val}")
        end
    end
end
if $errors.length > 0
    $errors.each do | e |
        puts e
    end
    exit(1)
else
    exit(0)
end
