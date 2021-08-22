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
- [ ] Send request to join a room
- [x] Create a new room
- [ ] Search rooms

#### Rooms

- [x] Create rooms where user becomes 'admin'
- [x] Add admins
- [x] Send messages in rooms created by other users
- [x] Create threads in created room
- [x] Send messages to threads in that room
- [ ] Search messages in threads
- [ ] (Room wide message search)
- [ ] (Server side pagination and filters)

#### Users/Access control

|                                 | as owner | as admin | as quest | done |
| ------------------------------- | -------- | -------- | ------------------------------- | ------------------------------- |
| can invite users                | yes             | yes | yes      |  |
| can accept users                | yes             | yes      | no       |  |
| can initiate a thread           | yes        | yes      | no       | :heavy_check_mark: |
| can delete other users messages | yes | yes      | no       |        |
| can delete own messages         | yes      | yes      | yes      |       |
| can send messages to a thread   | yes | yes      | yes       | :heavy_check_mark: |
| can add admins | yes | yes | no | :heavy_check_mark: |

