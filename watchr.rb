watch('./(.*).py')  { |m| code_changed(m[0]) }

def code_changed(file)
  run "clear && nosetests tests/unit/"
end

def run(cmd)
  result = `#{cmd}`
  growl result rescue nil
end

def growl(message)
  puts(message)
  message = message.split("\n").last(3);
end
