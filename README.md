# pi-power-reset-buttons

Build on scripts from pi-power-button

See their official [Raspberry Pi power button guide](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi).

## Installation (for this repo)

1. Connect to your Raspberry Pi via SSH
1. Clone this repo: `git clone https://github.com/yieldpoint/pi-power-button.git`
1. Run the setup script: `./pi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script in order to use GPIO2/3 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`

## Hardware

You'll need two normally-open (NO) power buttons. 

To test, connect a jumper to ground, and touch pin 3 for restart, 5 for shutdown.
Final will have pin 3 and 5 connected to button passthroughs on the cape
