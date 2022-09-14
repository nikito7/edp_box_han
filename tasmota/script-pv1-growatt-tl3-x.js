>D

bug="fix"
wfc=""
wfp=0
cnt=0

>B

tper=31
smlj=0

=>Delay 100
=>SerialLog 0
=>WifiConfig
=>WifiPower

=>Delay 100
=>Sensor53 r

>E

wfc=WifiConfig#?
wfp=WifiPower

>S

if cnt==40
then
smlj=1
tper=15
=>UfsRun discovery.txt
endif

if cnt<99
then
cnt+=1
endif

>W

@<b>Vars </b> cnt=%0cnt% tper=%0tper% smlj=%0smlj%
@<b>Wifi </b> %wfc% <b> Power </b> %0wfp% <b> Topic </b> %topic%
@<br>

; inverter growatt tl3-x

>M 1

+1,3,mN1,1,9600,PVx,1,15,r010400000003,r010400370002,r010400270003,r0104005D0003

; 0x0000 0,1,2

1,010406UUuu@i0:1,Inverter Status,,PV_Status,0
1,010406xxxxUUuuUUuu@i0:10,Input Power,W,*,1

; 0x0027 35-36,37

1,010406UUuuUUuu@i1:10,Output Power,W,*,1
1,010406xxxxxxxxUUuu@i1:10,Frequency,Hz,*,2

; 0x0037 55-56

1,010404UUuuUUuu@i2:10,Total Energy,kWh,PV_Energy,1

1,=h<br>

; 0x005D 93-95

1,010406UUuu@i3:10,Temp 1,°C,*,1
1,010406xxxxUUuu@i3:10,Temp 2,°C,*,1
1,010406xxxxxxxxUUuu@i3:10,Temp 3,°C,*,1

; eof meter

#

; eof script 
; check code 17:45

