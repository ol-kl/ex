# Average Home Computer Data Transfer Speed
## Memory (DDR SDRAM)

Transfer Rate (MB/s) = I/O FBS clock (MHz) * 2 (Rising and Falling edges) * FBS width (bytes) 

Example for DDR3-1600: Transfer Rate (MB/s) = 800 * 2 * 8 = 12800 MB/s

To transfer 1 MB: ~100us
## Secondary Storage (HDD/SSD) to Memory transfer

Secondary Storage (Disk-to-Buffer)-> SATA3 -> DMI (South - North Bridge Interconnect) -> Memory

SATA3 HDD: 150 MB/s for sequential read (+ Seek Time 10ms, Rotational Latency 5 ms)

SATA3 SSD: 400 MB/s for read (Random Access time < 0.1ms)

SATA3 BW: 600 MB/s

DMI 2: 2.0 GB/s (all 4 lanes in use, no contention)

Memory DDR3-1600: 12800 MB/s

Hence data transfer rate from Secondary storage to Memory is limited by the storage data transfer rate.

To transfer 1 MB from HDD to Memory: 7ms + 15ms (Seek Time + Rotation Latency) = 22 ms

To transfer 1 GB from HDD to Memory: 6.7s + 15ms (Seek Time + Rotation Latency) = 6.85 s

To transfer 1 MB from SSD to Memory: 2.5ms

To transfer 1 GB from SSD to Memory: 2.5s
