Name: cookbook-test
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Just a cookbook to test builds

License: AGPL 3.0
URL: https://github.com/redBorder/cookbook-example
Source0: %{name}-%{version}.tar.gz

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/var/chef/cookbooks/test
cp -f -r  resources/* %{buildroot}/var/chef/cookbooks/test
chmod -R 0755 %{buildroot}/var/chef/cookbooks/test
install -D -m 0644 README.md %{buildroot}/var/chef/cookbooks/test/README.md

%pre
if [ -d /var/chef/cookbooks/test ]; then
    rm -rf /var/chef/cookbooks/test
fi

%post
case "$1" in
  1)
    # This is an initial install.
    :
  ;;
  2)
    # This is an upgrade.
    su - -s /bin/bash -c 'source /etc/profile && rvm gemset use default && env knife cookbook upload test'
  ;;
esac

%postun
# Deletes directory when uninstall the package
if [ "$1" = 0 ] && [ -d /var/chef/cookbooks/test ]; then
  rm -rf /var/chef/cookbooks/test
fi

%files
%defattr(0644,root,root)
%attr(0755,root,root)
/var/chef/cookbooks/test
%defattr(0644,root,root)
/var/chef/cookbooks/test/README.md

%changelog
* Fri Aug 8 2025 manegron <manegron@redborder.com>
- first spec version
