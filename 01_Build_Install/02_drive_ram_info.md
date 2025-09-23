# Checking SSD and HDD Drives 
Install smartmontools:
```bash
sudo apt install smartmontools
```

List your devices:
```bash
sudo smartctl --scan
```

Run a short self-test and check overall health:
```bash
sudo smartctl -t short /dev/sdX
sudo smartctl -H /dev/sdX
```

Print all SMART and non-SMART information for device:
```bash
sudo smartctl -a /dev/sdX
```

### For Mechanical HDD Check the following values:  
- Capacity: >=1.00 TB
- Rotation Rate: >=5400 rpm
- SATA Version: >=SATA 3.0, 6.0 Gb/s
- SMART overall-health self-assessment test result: PASSED
- Reallocated_Sector_Count: 0

### For SSD Check the following values:  
- Capacity: >=1.00 TB
- SATA Version: >=SATA 3.0, 6.0 Gb/s
- SMART overall-health self-assessment test result: PASSED
- Wear_Leveling_Count: Low Value is Better
- Available_Spare: >=10%
- Percentage_Lifetime_Remaining: >=10%

# Checking RAM
You can use the `dmidecode` command to output information on your RAM.
```bash
sudo dmidecode -t memory
```
For each Memory Device it will list:  
- Type: like DDR3
- Size: in MB
- Speed: in MHz
- Serial Number: useful for looking up CAS on web

The only other way to find the CAS Latency is to read it off of the label on the chip or to look it up in BIOS.