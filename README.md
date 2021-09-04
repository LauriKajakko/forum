# Forum

# https://tsoha---forum.herokuapp.com/

## Overview
Create rooms with threads to message other users!

## Instructions

1. reqister
2. create a room for yourself
3. create a thread
4. post messages
5. go to room settings to add admins from users list

* private rooms and invitations not yet implemented

## Features

#### Main page

- [x] Browse rooms created by other users
- [x] Create a new room

#### Rooms

- [x] Create rooms where user becomes 'admin'
- [x] Add admins
- [x] Send messages in rooms created by other users
- [x] Create threads in created room
- [x] Send messages to threads in that room
- [x] Search users in rooms settings
- [x] (Server side pagination)

#### Profile page
- [x] Stats of messages, rooms etc.
- [ ] Links to rooms


#### Users/Access control

|                                 | as owner | as admin | as quest | done |
| ------------------------------- | -------- | -------- | ------------------------------- | ------------------------------- |
| can initiate a thread           | yes        | yes      | no       | :heavy_check_mark: |
| can delete other users messages | yes | yes      | no       |        |
| can delete own messages         | yes      | yes      | yes      |       |
| can send messages to a thread   | yes | yes      | yes       | :heavy_check_mark: |
| can add admins | yes | yes | no | :heavy_check_mark: |

