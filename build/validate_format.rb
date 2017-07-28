#!/usr/bin/env ruby

auth_keys = ['apiKey', 'OAuth', 'X-Mashape-Key', 'No']
punctuation = ['.', '?', '!']
https_keys = ['Yes', 'No']
args = ARGV
filename = args[0]
$errors = []

def add_error(line_num, message)
    $errors.push("(L%03d) #{message}" % line_num)
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
                    case val_index
                    when 1
                        msg = "spacing on Title is invalid"
                    when 2
                        msg = "spacing on Description is invalid"
                    when 3
                        msg = "spacing on Auth is invalid"
                    when 4
                        msg = "spacing on HTTPS is invalid"
                    when 5
                        msg = "spacing on Link is invalid"
                    end
                end
            end
            if msg != ""
                add_error(line_num, "#{msg} (pad before and after string)")
            end
        end

        ################# DESCRIPTION ################
        # First character should be capitalized
        desc_val = values[2].lstrip.chop
        if !/[[:upper:]]/.match(desc_val[0])
            add_error(line_num, "invalid Description (first char not uppercase): #{desc_val}")
        end
        # value should not be punctuated
        last_char = desc_val[desc_val.length-1]
        if punctuation.include?(last_char)
            add_error(line_num, "invalid Description (description should not end with \"#{last_char}\")")
        end
        #################### AUTH ####################
        # Values should conform to valid options only
        auth_val = values[3].lstrip.chop.tr('``', '')
        if !auth_keys.include?(auth_val)
            add_error(line_num, "invalid Auth (not a valid option): #{auth_val}")
        end
        #################### HTTPS ###################
        # Values should be either "Yes" or "No"
        https_val = values[4].lstrip.chop
        if !https_keys.include?(https_val)
            add_error(line_num, "invalid HTTPS (must use \"Yes\" or \"No\"): #{https_val}")
        end
        #################### LINK ####################
        # Url should be wrapped in "[Go!]" view
        link_val = values[5].lstrip.chop
        if !link_val.start_with?("[Go!](") || !link_val.end_with?(')')
            add_error(line_num, "invalid Link (format should be \"[Go!](<LINK>)\"): #{link_val}")
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
