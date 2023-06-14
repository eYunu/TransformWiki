
## Useful Commands
1. docker compose up --build
2. pip freeze > requirements.txt
3. Generate SSH:
   1. cd to ~/.ssh
   2. ssh-keygen -b 4096    //or:
   3. ssh-keygen -t ed25519 -b 4096 -C "{username@emaildomain.com}" -f {ssh-key-name}
   4. ssh-copy-id username@public_ip_address
   5. ssh -i ~/.ssh/id_rsa username@public_ip_address
   6. copy the keyname.pub then paste it to the ssh server
4. Others tips:
   1. exec ssh-agent bash
   2. ssh-add ~/gdsshkey_vps
5. Docker runtime commands:
   1. docker exec -it <CONTAINER_ID> /bin/bash
      1. Example to create admin user in docker runtime:
         1. docker ps //to list all docker images
         1. docker exec -it 3beaade9475b /bin/bash
         2. python manage.py createsuperuser
   2. Restart docker-compose:
      1. docker-compose restart celery


6. Linux cmd (ubuntu):
   1. sudo apt-get install update


7. Setting git SSH in linux server:
   1. https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/
   2. e.g: 
      1. ssh-keygen -t ed25519 -b 4096 -C "yinyeo.ng.dds@gmail.com" -f gdv2azuregit
      2. enter passphrase: dds123
      3. Your identification has been saved in gdv2azuregit
         Your public key has been saved in gdv2azuregit.pub
         The key fingerprint is:
         SHA256:+8g0FxrgL9yaVk0xIYc7ftzPuRZkHU/NFjtxt4z3Cc0 yinyeo.ng.dds@gmail.com
         The key's randomart image is:
         +--[ED25519 256]--+
         |        ..o.   +=|
         |        .oo   =.@|
         |      .  . o o Eo|
         |     . .o .   = *|
         |      ..S=.. o ..|
         |     . oo++.. .  |
         |      o.B..  o o |
         |      .* =    =  |
         |     .o o .  ... |
         +----[SHA256]-----+
      4. exec ssh-agent bash
      5. ssh-add ~/gdsshkey_vps
      6. Then add the fingerprint to bitbucket (whole line including the email)
      7. test connection: ssh -T git@bitbucket.org
      8. 