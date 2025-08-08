# Cookbook:: test
# Provider:: config

include Test::Helper

action :add do
  begin
    Chef::Log.info('cookbook test (add) has been processed')
  rescue => e
    Chef::Log.error(e.message)
  end
end

action :remove do
  begin
    Chef::Log.info('cookbook test (remove) has been processed')
  rescue => e
    Chef::Log.error(e.message)
  end
end
