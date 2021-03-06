# Linux Workshop

In this workshop you will get an introduction to the Linux environment. We'll go
through the installation (using a virtual machine) and usage of basic commands
on the Terminal. To finish off we will configure Cron to do a task automatically
for us.

## Goals

After the workshop the participants should have grasped concepts and developed
skills as follows.

- Understand what are:

  - Operating systems
  - Linux systems
  - Virtual machines

- Know how to:
  - Install and use a hypervisor
  - Perform basic tasks in a Linux environment
  - Use Cron jobs

## Structure

- Operating Systems

  - What is an Operating System?
    - Basic explanation
    - **Exercise:** What are some examples of OS? (5 min)
  - GNU/Linux
    - Open Source software
    - What are distributions?
    - **Exercise:** Find 2 distributions you find interesting (10-15 min)
    - Ubuntu
  - What is Linux used for?
    - All [Android](<https://en.wikipedia.org/wiki/Android_(operating_system)>)
      phones and tablets (including the ones on the plane seats)
    - Basically all web servers everywhere (including Google, Amazon,
      Facebook...), and any other professional network server for that matter
    - DevOps / Docker
    - [Software Development](https://snapcraft.io/search?category=development)
    - Robotics / Raspberry Pi / Car systems
      ([Tesla](https://www.tesla.com/careers/job/software-engineerembeddedlinuxplatforms-45034))
    - Scientific research / Data mining / General number crunching
    - Animating, apparently
      - [Real-Time Graphics in Pixar Film
        Production](https://www.youtube.com/watch?v=x9ikzGQW0ys)
    - Hmmm... to power the [International Space
      Station](https://training.linuxfoundation.org/solutions/corporate-solutions/success-stories/linux-foundation-training-prepares-the-international-space-station-for-linux-migration/)?
    - Desktop OS

- Virtual Machines

  - What is a Virtual Machine?
  - What are Hypervisors?
  - Virtualbox
  - What are VMs used for?
  - Cloud services
    - Create an instance in AWS or DO

- Linux
  - Install Ubuntu with VirtualBox (check the Resources section below)
  - Ubuntu Overview
    - Graphical interface overview
    - System configuration tool
    - Common applications & How to install new ones
  - Linux overview
    - Folder structure overview
    - Basic command line usage
      - whoami, whatis, whereis
      - cd, pwd, mkdir, ls -l, cp, cp -R, mv, rm, rm -R
      - cat, more
      - df -h, du -sh
      - find . -name caffeine.txt
      - top, kill
      - exit
    - Use the man command:
      - man man / man ls (How to list by size?)
    - Wild cards
      - ls \*.txt
    - Package manager
      - apt
        - cowsay
    - Editing files with vim
      - Modes
      - Save, quit
    - Network Operations
      - Ping
      - Nmap google.com
- Cron jobs
  - What are Cron jobs?
  - Exercise
    - Create python script to update a file
    - Make cron update it every 10 seconds
    - Extra challenge: send an email to someone every hour with a new quote (or
      whatever)

## Resources

- Downloads

  - [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
    (Pick an option from “VirtualBox platform packages”)
  - [https://ubuntu.com/download](https://ubuntu.com/download) (Download Ubuntu
    Desktop)

- Sources

  - [https://en.wikipedia.org/wiki/Operating_system](https://en.wikipedia.org/wiki/Operating_system)
  - [https://en.wikipedia.org/wiki/Virtual_machine](https://en.wikipedia.org/wiki/Virtual_machine)
  - [https://en.wikipedia.org/wiki/Linux](https://en.wikipedia.org/wiki/Linux)
  - [https://en.wikipedia.org/wiki/Open-source_software](https://en.wikipedia.org/wiki/Open-source_software)
  - [https://en.wikipedia.org/wiki/Cron](https://en.wikipedia.org/wiki/Cron)
  - [Best virtual machine software of 2020: virtualization for different
    OS](https://www.techradar.com/best/best-virtual-machine-software)
  - [What virtualization technology is set up on
    VPS?](https://www.namecheap.com/support/knowledgebase/article.aspx/909/48/what-virtualization-technology-is-set-up-on-vps/)
  - [The Linux Directory Structure,
    Explained](https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/)
  - [How to find out the virtualization type of an linux VPS?
    ](https://serverfault.com/questions/595471/how-to-find-out-the-virtualization-type-of-an-linux-vps)
  - [37 Important Linux Commands You Should
    Know](https://www.howtogeek.com/412055/37-important-linux-commands-you-should-know/)
  - [Scheduling Tasks with Cron
    Jobs](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800)

* Further learning

  - [LINUX Exercises, Exams, Challenges](https://practity.com/lynux/)
  - [35 Linux Basic Commands Every User Should Know](https://www.hostinger.in/tutorials/linux-commands)
  - [Linux Journey](https://linuxjourney.com/)
  - [Start Learning Linux in
    Minutes](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/)
  - [9 Free Linux Training Courses For
    Everyone](https://itsfoss.com/free-linux-training-courses/)
  - [Linux Foundation Learning
    Center](https://training.linuxfoundation.org/resources/free-courses/introduction-to-linux/)
  - [Create and Run Your First Bash Shell Script](https://linuxhandbook.com/run-shell-script/)
  - Random stuff
    - [Text-based
      games](https://www.tecmint.com/best-linux-terminal-console-games/)
    - [Useless but fun terminal
      commands](https://www.tecmint.com/20-funny-commands-of-linux-or-linux-is-fun-in-terminal/)

* Multimedia
  - Explainer - [What is an Operating System as Fast As
    Possible](https://www.youtube.com/watch?v=pVzRTmdd9j0)
  - Movie - [Revolution OS](https://www.youtube.com/watch?v=PcdnamUOeaA), about
    the beginning of free Free Software Movement
