# pyramid-zappa-api-boilerplate
A Python boilerplate for creating AWS Lambda API projects using Pyramid and Zappa, orchestrated with Ansible.

## Overview
We're all working quite a bit with Python and AWS Lambda. In order to create our countless APIs, ETL scripts, Chat Bots,
etc. we want a boilerplate project that we can share. The hope is that we can share this project amongst ourselves to
make this development easier.

We're deciding to use Zappa and Pyramid as our frameworks of choice to make this happen.

### Pyramid
The Pyramid Framework is a relatively small framework that handles the minimal request/response style web app. It's not
too opinionated and bulky, but opinionated and feature rich enough out of the box to make our lives easier. The hope is
that it will provide us just what we need, but still allow us plenty of runway to grow over time.

Homepage: [Pyramid Homepage](https://trypyramid.com)

### Zappa
Zappa is a library/framework will allow us to develop server-less python web services, specifically for tying into AWS
Lambda and AWS API Gateway. We will have some challenges in regards to how to manage the various production environments
while not checking everything directly into the code base. This is one of the major reasons for trying to create a
bootstrap process that allows us to quickly iterate without re-inventing the wheel every time; we need to properly
answer a lot of the tough questions so that when it comes time to implement the code, we have a lot of the hard
questions answered.

GitHub Repo: [Zappa Project](https://github.com/Miserlou/Zappa)

## Goal
The primary goal of this project is to create an easy to use project boilerplate for developing projects built
upon Pyramid / Zappa (Python & AWS Lambda). It should be opinionated enough to save work, while not being too strict
that only one person will ever want to use it.

## Requirements
  1. Python 3.6 (AWS Lambda Runtime)
  1. Vagrant backed Development Environment
  1. Ansible Infrastructure Management
  1. Pre-compiled Python Vagrant Box using latest Ubuntu
  1. Strong documentation on how to build on top of this boilerplate
  1. Opinionated Python style guide
  1. Proper code examples / mini projects for reference
     * basic REST API using standard CRUD operations with proper verbs (GET/PUT/POST/DELETE ... etc)
  1. Opinionated management of environments and configuration
  1. Opinionated management of testing (unit and integration)
  1. Opinionated Database access / management / modeling options
  1. Opinionated Logging structures (Slack, CloudWatch, etc.)
  1. Configuration should be managed by Environment variables
     * Sample "config" files should be stored in the repository, but no actual variables

## Child Projects / Requirements
Below is a list of child projects / modules that we'll want to build to work with this boilerplate

  1. JWT support for REST APIs
  1. Authentication/Authorization Module (Passport based?)
  
