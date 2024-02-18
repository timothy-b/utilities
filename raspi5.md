# Resources I used for setting up my Raspberry Pi 5

PCIe to NVME adapter:

https://geekworm.com/products/x1001

For enabling boot from NVMe and controlling boot order:

https://www.jeffgeerling.com/blog/2023/nvme-ssd-boot-raspberry-pi-5

For setting up BTRFS + LUKS on the NVME:

https://www.raspberrypi.com/documentation/computers/raspberry-pi-5.html#booting-from-pcie

https://mutschler.dev/linux/raspi-btrfs/

https://wiki.geekworm.com/NVMe_SSD_boot_with_the_Raspberry_Pi_5

If you don't have `cryptroot-unlock` in the path, link it from `/usr/share/cryptsetup/initramfs/bin/`.

Also, `/etc/dropbear-initramfs` is now `/etc/dropbear/initramfs`.

Also, set `space_cache` to `space_cache=v2` in `/etc/fstab` or else the root partition will be mounted read-only.

Then set the second partion to be swap.

For setting up a window manager (I used RPD (LXDE)):

https://forums.raspberrypi.com/viewtopic.php?t=133691

also install `lxterminal`

For fixing `startx` error:

https://github.com/KlipperScreen/KlipperScreen/issues/349

LXDE window control keybindings:

http://openbox.org/wiki/Help:Actions#GoToDesktop

If you use `obconf` and it breaks settings, exit X to console and rename `~/.config/openbox/lxde-pi-rc.xml`.
