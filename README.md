<div align="center">

# PiEEG-8

**Turn a Raspberry Pi into an 8-channel brain-computer interface.**

Open-source Raspberry Pi shield for measuring EEG, EMG and ECG with the TI ADS1299.

[📖 Documentation](https://docs.pieeg.com/hardware/devices/pieeg-8/) ·
[🚀 How to Start](https://docs.pieeg.com/hardware/devices/pieeg-8/setup/) ·
[🛒 Buy](https://pieeg.com/) ·
[💬 Discord](https://discord.gg/5Ps24p47)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_on_pi.jpg" alt="PiEEG-8 shield on a Raspberry Pi" width="420">

</div>

> [!WARNING]
> PiEEG-8 is **not a medical device** and has not been certified by any regulator for use with the human body. It is a tool for research, education and engineering. You use it at your own risk.

> [!CAUTION]
> **Battery only.** The Raspberry Pi, the shield and everything cabled to them (monitor, keyboard) must run from a **5 V power bank** while electrodes are on a person. Never use a wall charger or a mains-powered monitor or computer. The board has **no isolation**. Read the [Safety page](https://docs.pieeg.com/hardware/devices/pieeg-8/safety/) and the [liability notice](https://pieeg.com/liability/).

## At a glance

| | |
|---|---|
| **Channels** | 8 biosignal inputs, plus reference and bias |
| **Converter** | TI ADS1299, 24-bit, simultaneous sampling |
| **Sample rate** | 250 SPS (default) |
| **Signals** | EEG, EMG, ECG |
| **Host** | Raspberry Pi 4 or Raspberry Pi 5 |
| **Link to the Pi** | SPI0 on the 40-pin header, DRDY on GPIO 26 |
| **Electrodes** | Dry or wet Ag/AgCl, 2.54 mm header |
| **Power** | 5 V power bank, 3 A, up to 10,000 mAh |
| **Software** | [PiEEG Server](https://github.com/pieeg-club/PiEEG-server), Python SDK (this repo), [BrainFlow](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#pieeg) |

## How it works

```
 Electrodes 1–8 ─┐
 Reference (ear) ┼─► PiEEG-8 ─SPI─► Raspberry Pi ─► PiEEG Server
 Bias (ear) ─────┘   (ADS1299)      4 or 5          ├ dashboard :1617
                                      ▲             ├ WebSocket :1616
             5 V power bank ──────────┘             └ CSV · LSL · OSC
```

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_setup.png" alt="PiEEG-8 setup: cap, shield on the Pi, power bank, monitor, keyboard and mouse" width="700">

## Quick start

1. **Mount** the shield on the Raspberry Pi's 40-pin header (Pi switched off).
2. **Connect** 8 electrodes to channels 1–8, a reference ear clip and a bias ear clip.
3. **Power** the Pi from a 5 V power bank. The LED on the shield lights up.
4. **Install and run** [PiEEG Server](https://github.com/pieeg-club/PiEEG-server):

```bash
curl -sSL https://raw.githubusercontent.com/pieeg-club/PiEEG-server/main/install.sh | bash
sudo reboot                          # first time only: enables SPI
pieeg-server --device pieeg8
```

5. **Open** `http://raspberrypi.local:1617`, click **Connect**, close your eyes and watch the alpha rhythm rise.

> [!NOTE]
> The installer's background service starts in 16-channel mode. To make it start as PiEEG-8, see [How to Start](https://docs.pieeg.com/hardware/devices/pieeg-8/setup/#install-and-start-pieeg-server).

Full walkthrough: **[docs.pieeg.com → PiEEG-8 → How to Start](https://docs.pieeg.com/hardware/devices/pieeg-8/setup/)**

## Wiring

| Input | Electrode | Purpose |
|---|---|---|
| **Channels 1–8** | EEG electrodes in a cap (10-20 system) | Signal |
| **Reference** | Ear clip on one earlobe | Common 0 µV point for all channels |
| **Bias** | Ear clip on the other earlobe | Cancels common-mode noise (mains hum) |

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_connection.png" alt="Wiring of channels 1–8, reference and bias" width="700">

### Raspberry Pi pinout

| Header pin | GPIO | Signal |
|---|---|---|
| 19 | GPIO 10 | SPI0 MOSI |
| 21 | GPIO 9 | SPI0 MISO |
| 23 | GPIO 11 | SPI0 SCLK |
| 24 | GPIO 8 | SPI0 CE0 |
| 37 | GPIO 26 | DRDY (data ready) |

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_pinout.png" alt="PiEEG-8 SPI and DRDY pins on the 40-pin header" width="600">

## Software

| | Best for |
|---|---|
| **[PiEEG Server](https://github.com/pieeg-club/PiEEG-server)** (recommended) | Browser dashboard, recording, WebSocket, LSL, VRChat OSC, webhooks |
| **Python SDK** (this repo, [`1.GUI`](1.GUI)) | Learning the ADS1299, raw data, custom register settings |
| **[BrainFlow](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#pieeg)** | `BoardIds.PIEEG_BOARD` (ID 56); build BrainFlow on the Pi with `--build-periphery` |

### Python SDK scripts

| Script | Pi | What it does |
|---|---|---|
| [`1.8_ch_Pi5.py`](1.GUI/1.8_ch_Pi5.py) | Pi 5 | Live 8-channel graph, band-pass filtered (system `python3-libgpiod`) |
| [`1.8_ch_Pi5_gpiod_1_5_4.py`](1.GUI/1.8_ch_Pi5_gpiod_1_5_4.py) | Pi 5 | Same, for `pip install gpiod==1.5.4` |
| [`1.8_ch_Pi4.py`](1.GUI/1.8_ch_Pi4.py) | Pi 4 | Live 8-channel graph, band-pass filtered |
| [`Raw_data_1Ch_Pi5.py`](1.GUI/Raw_data_1Ch_Pi5.py) | Pi 5 | Raw view of one channel |
| [`save_data_short_Pi5.py`](1.GUI/save_data_short_Pi5.py) | Pi 5 | Save raw µV to Excel |
| [`save_data_gpiod_1_5_4.py`](1.GUI/save_data_gpiod_1_5_4.py) | Pi 5 | Save raw µV to Excel, `gpiod==1.5.4` |
| [`save_data_short_Pi4.py`](1.GUI/save_data_short_Pi4.py) | Pi 4 | Save raw µV to Excel |

**Install** (recent Raspberry Pi OS needs a virtual environment):

```bash
python3 -m venv --system-site-packages ~/pieeg-env
source ~/pieeg-env/bin/activate
pip install spidev matplotlib scipy pandas openpyxl

# Raspberry Pi 5 — pick one:
sudo apt install -y python3-libgpiod      # for 1.8_ch_Pi5.py
pip install gpiod==1.5.4                  # for 1.8_ch_Pi5_gpiod_1_5_4.py

# Raspberry Pi 4:
pip install RPi.GPIO
```

**Run:**

```bash
cd 1.GUI
python 1.8_ch_Pi5.py          # or 1.8_ch_Pi4.py
```

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_gui.jpg" alt="Live 8-channel graph" width="500">

Details, troubleshooting and the data format: **[Software docs](https://docs.pieeg.com/hardware/devices/pieeg-8/software/)** · **[Specification](https://docs.pieeg.com/hardware/devices/pieeg-8/specification/)**

## Example signals

**EEG: alpha rhythm** (eyes closed)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_alpha.png" alt="Alpha rhythm with eyes closed" width="700">

**EEG: chewing and blinking artifacts**

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_artifacts.png" alt="Chewing and blinking artifacts" width="700">

**EMG** and **ECG**

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_emg.jpg" alt="EMG" width="49%"> <img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_ecg.png" alt="ECG" width="49%">

## What's in this repository

| Folder | Content |
|---|---|
| [`1.GUI`](1.GUI) | Python SDK: live graphs and saving data for Raspberry Pi 4 and 5 |
| [`1.GUI/dataset`](1.GUI/dataset) | Raw EEG with chewing and blinking (4-3-2-1 times), plus plotting scripts |
| [`Datasets`](Datasets) | Raw EEG with dry Ag/AgCl electrodes, 250 SPS |
| [`2.Software`](2.Software) | Legacy PiEEG desktop app and data-conversion scripts |
| [`ML_application`](ML_application) | Machine-learning example: record → alpha power → classifier |
| [`images`](images) | Images used in the original README |
| [`Manual. Conenction and start - PiEEG1.pdf`](Manual.%20Conenction%20and%20start%20-%20PiEEG1.pdf) | Printable quick-start manual |
| [`Wet EEG cap - How to use it.pdf`](Wet%20EEG%20cap%20-%20How%20to%20use%20it.pdf) | Instructions for the wet-electrode cap |

## Documentation

| Page | |
|---|---|
| [PiEEG-8 Intro](https://docs.pieeg.com/hardware/devices/pieeg-8/) | Overview and specs at a glance |
| [What's in the Box](https://docs.pieeg.com/hardware/devices/pieeg-8/required-equipment/) | What you need besides the shield |
| [How to Start](https://docs.pieeg.com/hardware/devices/pieeg-8/setup/) | Step-by-step setup and first signal checks |
| [Electrodes & Pinout](https://docs.pieeg.com/hardware/devices/pieeg-8/connections/) | Wiring, montage, GPIO pins |
| [Software](https://docs.pieeg.com/hardware/devices/pieeg-8/software/) | PiEEG Server, Python SDK, BrainFlow |
| [Signals & Datasets](https://docs.pieeg.com/hardware/devices/pieeg-8/examples/) | Example recordings, datasets, ML example |
| [Specification](https://docs.pieeg.com/hardware/devices/pieeg-8/specification/) | Data frame, µV conversion, ADS1299 registers |
| [Troubleshooting](https://docs.pieeg.com/hardware/devices/pieeg-8/troubleshooting/) | Fixes for SPI, GPIO, software and noise |
| [Safety](https://docs.pieeg.com/hardware/devices/pieeg-8/safety/) | Battery-only operation and responsible use |

## Video

[![How to start with PiEEG](https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/pieeg8_video.jpg)](https://youtu.be/zOxcixEGeE8)

## Citation

If you use PiEEG-8 in research, please cite:

```
I. Rakhmatulin et al. PIEEG: Turn a Raspberry Pi into a Brain-Computer-Interface
to measure biosignals. arXiv:2201.02228, 2022.

I. Rakhmatulin et al. Raspberry Pi Shield – for measure EEG (PIEEG). 2021 5th International
Conference on Electrical, Electronics, Communication, Computer Technologies and Optimization
Techniques (ICEECCOT), pp. 410–413. DOI: 10.1109/ICEECCOT52851.2021.9707969
```

## License

Software and SDK: **MIT**. Hardware use is subject to the terms in [`license.txt`](license.txt) and the [PiEEG liability notice](https://pieeg.com/liability/).

## Contact

- 🌐 [pieeg.com](https://pieeg.com/)
- 📖 [docs.pieeg.com](https://docs.pieeg.com/)
- 💬 [Discord](https://discord.gg/5Ps24p47)
- ✉️ [pieeg@pieeg.com](mailto:pieeg@pieeg.com)
