# Forum

# https://tsoha---forum.herokuapp.com/

## Instructions

1. reqister
2. create a room for yourself
3. create a thread
4. post messages
5. do the same with another user to see how access control works *

* private rooms and invitations not yet implemented

## Features

#### Main page

- [x] Browse rooms created by other users
- [ ] Send request to join a room
- [x] Create a new room
- [ ] Search rooms

#### Rooms

- [x] Create rooms where user becomes 'admin'
- [ ] Add admins
- [ ] Join rooms created by other users
- [x] Create threads in created room
- [x] Send messages to threads in that room
- [ ] Search messages in threads
- [ ] (Room wide message search)
- [ ] (Server side pagination and filters)

#### Users/Access control

|                                 | as admin | as quest |
| ------------------------------- | -------- | -------- |
| can invite users                | yes      | yes      |
| can accept users                | yes      | no       |
| can initiate a thread           | yes      | no       |
| can delete other users messages | yes      | no       |
| can delete own messages         | yes      | yes      |
| can mute users                  | yes      | no       |
| can send messages to a thread   | yes      | no       |

