# NetDevOps Labs

Welcome to the NetDevOps training lab module! This repository contains demo scripts and practice labs that accompany the network automation training course.

*For access to the slides please reach out to the maintainer. The labs and demo material in this repository can be used independently as well for any of the individual topics.*

## Overview

This repository is designed to help you practice and gain hands-on experience in various network automation technologies. The labs are divided into three phases, each covering essential topics:

- Python3
- Jinja2 templating
- JSON
- EAPI
- CVP REST APIs
- cvprac
- Git
- Ansible
- ansible-eos collection
- ansible-cvp collection
- ansible-avd collection

*The labs are designed to be run on a ATD (Arista Test Drive) enviroment, but with changes to the login credentials and IPs can be used with a different virtual (veos-lab, cEOS-Lab) or physical setup as well.*

## Phase 1 - Fundamentals

In Phase 1, you will find demo and lab modules covering the following topics:

- CVP REST APIs
- cvprac
- JSON
- EAPI
- YAML
- JINJA2
- Basics of Git

## Phase 2 - Ansible Essentials

Phase 2 includes demo and lab modules for the following topics:

- Ansible Basics
  - Inventory
  - Ad hoc commands
  - Variables
  - Tasks
  - Playbooks
  - Roles
  - Conditionals
  - Loops
  - Ansible Modules
  - Collections
    - Arista EOS Collection
    - Arista CVP Collection

## Phase 3 - Advanced Topics

Phase 3 contains demo and lab modules focusing on the following topics:

- Arista ansible AVD collection
  - Single DC L3LS EVPN/VXLAN Symmetric IRB (eBGP overlay & eBGP underlay) deployment with eAPI
  - Single DC L3LS EVPN/VXLAN Symmetric IRB (iBGP overlay & OSPF underlay) deployment with CVP

## Getting Started

Follow these steps to get started with the labs:

- Open the `Programmability IDE` in your ATD web interface.
- Open a new terminal and run the following command to clone this repository

```shell
cd /home/coder/project/labfiles
git clone https://github.com/UchihaItachiSama/netdevops-lab.git
```

- The instructions for each demo/lab is present in the README.md file

For any issues or queries please reach out to the maintainer or open a issue.
