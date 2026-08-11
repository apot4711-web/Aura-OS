#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="mrdos"
iso_label="MRDOS_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="Mrd-OS <https://github.com/apot4711-web/Mrd-OS>"
iso_application="Mrd-OS Live/Rescue System"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="mrdos"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr'
           'bios.syslinux.eltorito'
           'uefi-x64.systemd-boot.esp'
           'uefi-x64.systemd-boot.eltorito')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--auto-threads=logical' '--long' '-19')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/root/.gnupg"]="0:0:700"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
)
