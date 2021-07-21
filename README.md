# imagedit
I'll draw you a picture - You're trying to submit some application to a website and they want the photo to be of a specific dimension. Online sites can't be trusted. So why not run it in your own system? You don't have to run photoshop or similar app for this. I don't know if any easier solutions are available (other than sites which require you to UPLOAD). I didn't care to look it up. I just wanted to kill some time. Ok Bye :D

## Installation
`git clone <this repository>`
Wait for it....
`pip3 install -r requirements.txt`

## Usage
### 1. Resize with cm
`python3 imagedit.py <file-name> -c -w 3.5 -he 4.5`
`-c` - Centimeters
`-w` - Width
`-h` - Height

### 2. Resize with resolution
`python3 imagedit.py <file-name> -w 3.5 -he 4.5`
`-w` - Width
`-h` - Height
