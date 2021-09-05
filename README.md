# Forum

# https://tsoha---forum.herokuapp.com/

## Overview
This is a project for a [course](https://hy-tsoha.github.io/materiaali/) focusing on learning to use SQL using postgres and python with flask.

## Instructions

1. reqister
2. create a room for yourself
3. create a thread
4. post messages
5. go to room settings to add admins from users list

## Features

#### Main page

- [x] Browse rooms created by other users
- [x] Create a new room
- [x] Pagination on rooms

#### Rooms

- [x] Create rooms where user becomes 'admin'
- [x] Add admins
- [x] Send messages in rooms created by other users
- [x] Create threads in created room
- [x] Send messages to threads in that room
- [x] Search users in rooms settings
- [x] Server side pagination on threads

#### Profile page
- [x] Stats of messages, rooms etc.


#### Users/Access control

|                                 | as owner | as admin | as quest | 
| ------------------------------- | -------- | -------- | ------------------------------- | 
| can initiate a thread           | yes        | yes      | no       | 
| can delete room | yes | yes      | no       |        |
| can send messages to a thread   | yes | yes      | yes       | 
| can add admins | yes | yes | no | 

