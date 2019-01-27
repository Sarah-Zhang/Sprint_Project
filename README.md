# project_Sprint

### Sprint 0: Team Building

- Assignment:
  - Goal: Team Building
  - Deliverable: Writeup
  - Due: Jan 30 10:30

- Schedule:
  - Meeting: Jan 26 14:00-20:00
  - Delivered: Jan 30 10:30

### Sprint 1: Deploy Script

- Assignment:
  - Goal:
    - implement a robust `deploy` function in python that takes in the arguments `path_to_ssh_key_private_key`, `server-address`, `prefix` and does the following:
      1. SSH connect to server (an EC2 instance) with username `testtest`
      2. Clone the git repo to home directory
      3. Set crontab to run `sample script` every **5min**
      4. Logout
    - implement a robust `sample script` that takes the argument `prefix` given by `Deploy` and does the following:
      1. Open and process the file `\srv\runme\prefix`
      2. Extract `name` and `age` fields
      3. Write the results to `\srv\runme\prefix.txt` with a tab in between the two fields
  - Deliverable: `deploy.py`
  - Due: Feb 13

- Schedule:
  - Before Meeting: each member writes his own deploy function
  - Meeting: Feb 2 18:00-20:00 *rescheduled to* Feb 1 10:30-12:00
    - brainstorm about the edge cases and check if the `deploy` function can handle them
    - finalize a `deploy.py` file
    - work together on `sample script`
  - Deliverd: Feb 9 17:56 on canvas
- Code Review:
  - write something in README
  - modulize
  - put log file in appropriate directory

### Sprint 2: Flask Application
