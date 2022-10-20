from ZeroKaiScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120c.bin",                # FileName
        "c120c",                    # MapName
        "c120c",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 10, 0, 11],
    )

    BuildStringList((
        "c120c",                  # 0
        "Cunha",                  # 1
        "Ozelle",                 # 2
        "Bishop",                 # 3
        "Old Man Quine",          # 4
        "Amisa",                  # 5
        "Grace",                  # 6
        "Reins",                  # 7
        "Cruise Ship Guide",      # 8
        "Mithra",                 # 9
        "Yaqi",                   # 10
        "Misa",                   # 11
        "BOA Officer",            # 12
        "Program Director",       # 13
        "BOA Clerk",              # 14
        "Roy",                    # 15
        "Roy",                    # 16
        "Meiling",                # 17
        "Meiling",                # 18
        "Chairman Mors",          # 19
        "Parla",                  # 20
        "Momo",                   # 21
        "Elsa",                   # 22
        "Detective Emma",         # 23
        "Anton",                  # 24
        "Ricky",                  # 25
        "Tourist",                # 26
        "Boy",                    # 27
        "Tourist",                # 28
        "Tourist",                # 29
        "Tourist",                # 30
        "Tourist",                # 31
        "Girl",                   # 32
        "Tourist",                # 33
        "Tourist",                # 34
        "Aretha",                 # 35
        "Stefan",                 # 36
        "Street Performer",       # 37
        "Singer",                 # 38
        "Wald",                   # 39
        "Luganov",                # 40
        "Jed",                    # 41
        "Huey",                   # 42
        "Slash",                  # 43
        "Kilika",                 # 44
        "Lechter",                # 45
        "Cruise Ship",            # 46
        "Estelle",                # 47
        "Joshua",                 # 48
        "Wazy",                   # 49
        "Abbas",                  # 50
        "Testament",              # 51
        "Testament",              # 52
        "Testament",              # 53
        "Testament",              # 54
        "Testament",              # 55
        "Viper",                  # 56
        "Viper",                  # 57
        "Viper",                  # 58
        "Viper",                  # 59
        "Viper",                  # 60
        "Customer",               # 61
        "Customer",               # 62
        "Customer",               # 63
        "Customer",               # 64
        "Customer",               # 65
        "Customer",               # 66
        "Customer",               # 67
        "Customer",               # 68
        "Customer",               # 69
        "Customer",               # 70
        "Young Man",              # 71
        "Young Man",              # 72
        "Officer",                # 73
        "Officer",                # 74
        "Zeit",                   # 75
        "SE Controls",            # 76
        "Central Plaza",          # 77
        "West Street",            # 78
        "Administrative District",# 79
        "Residential District",   # 80
        "Entertainment District", # 81
        "East Street",            # 82
        "Downtown District",      # 83
        "Harbor District",        # 84
        "IBC",                    # 85
        "Station Street",         # 86
        "Back Alley",             # 87
        "Ursula Road",            # 88
        "East Crossbell Highway", # 89
        "West Crossbell Highway", # 90
        "Mainz Mountain Path",    # 91
    ))

    AddCharChip((
        "chr/ch22100.itc",                   # 00
        "chr/ch25200.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "apl/ch50168.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch06000.itc",                   # 06
        "chr/ch34600.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch21200.itc",                   # 09
        "chr/ch22800.itc",                   # 0A
        "chr/ch23200.itc",                   # 0B
        "chr/ch27600.itc",                   # 0C
        "chr/ch27602.itc",                   # 0D
        "chr/ch32200.itc",                   # 0E
        "chr/ch32500.itc",                   # 0F
        "chr/ch24200.itc",                   # 10
        "chr/ch24600.itc",                   # 11
        "chr/ch22000.itc",                   # 12
        "chr/ch21000.itc",                   # 13
        "chr/ch24500.itc",                   # 14
        "chr/ch21900.itc",                   # 15
        "chr/ch23900.itc",                   # 16
        "chr/ch21300.itc",                   # 17
        "chr/ch20300.itc",                   # 18
        "chr/ch20600.itc",                   # 19
        "chr/ch20800.itc",                   # 1A
        "chr/ch20900.itc",                   # 1B
        "chr/ch21202.itc",                   # 1C
        "chr/ch21502.itc",                   # 1D
        "chr/ch20700.itc",                   # 1E
        "chr/ch30500.itc",                   # 1F
        "chr/ch37300.itc",                   # 20
        "chr/ch37400.itc",                   # 21
        "chr/ch02100.itc",                   # 22
        "chr/ch30800.itc",                   # 23
        "chr/ch31700.itc",                   # 24
        "chr/ch10400.itc",                   # 25
        "chr/ch27100.itc",                   # 26
    ))

    DeclNpc(-3520,   0,       8720,    90,   257,  0x0, 0,   0,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21150,   90,   257,  0x0, 0,   2,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39670,   -2500,   -19380,  180,  277,  0x0, 0,   3,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(38440,   -2490,   -18080,  135,  261,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(180,     -680,    4130,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1590,    -700,    3920,    135,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(42450,   -2500,   2330,    235,  261,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(15300,   0,       12980,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(19780,   0,       -3300,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(19780,   0,       -6090,   270,  261,  0x0, 0,   38,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-16500,  0,       -9050,   180,  277,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(5540,    -700,    1010,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-15890,  0,       -6060,   225,  261,  0x0, 0,   13,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-17450,  0,       -9450,   135,  405,  0x0, 0,   9,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-15890,  0,       -6060,   225,  469,  0x0, 0,   28,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-18590,  0,       -700,    225,  389,  0x0, 0,   4,   0,   0,   3,   0,   31,  255,  0)
    DeclNpc(-14390,  0,       -7840,   225,  469,  0x0, 0,   29,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-16150,  0,       -10960,  0,    277,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-17540,  0,       -11370,  45,   405,  0x0, 0,   27,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(21450,   0,       3300,    0,    389,  0x0, 0,   30,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(21450,   0,       4690,    180,  389,  0x0, 0,   37,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-17800,  0,       13370,   180,  389,  0x0, 0,   31,  0,   0,   0,   0,   46,  255,  0)
    DeclNpc(-5380,   2000,    20700,   180,  261,  0x0, 0,   32,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(-6130,   2000,    22040,   180,  261,  0x0, 0,   33,  0,   0,   0,   0,   48,  255,  0)
    DeclNpc(-7290,   -10,     -8520,   270,  261,  0x0, 0,   16,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-9150,   -10,     -8520,   90,   261,  0x0, 0,   17,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-17910,  0,       920,     45,   261,  0x0, 0,   18,  0,   0,   9,   0,   37,  255,  0)
    DeclNpc(830,     -700,    1980,    90,   261,  0x0, 0,   19,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(300,     -700,    -1680,   90,   261,  0x0, 0,   20,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(1170,    -700,    -3100,   45,   261,  0x0, 0,   21,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(1870,    -700,    -3810,   45,   261,  0x0, 0,   22,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(40790,   -2500,   -1310,   315,  389,  0x0, 0,   23,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(40000,   -2500,   0,       135,  389,  0x0, 0,   9,   0,   0,   0,   0,   43,  255,  0)
    DeclNpc(27330,   0,       12110,   90,   389,  0x0, 0,   24,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(27330,   0,       10480,   90,   389,  0x0, 0,   25,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(8250,    100,     80,      270,  453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(8250,    100,     80,      270,  453,  0x0, 0,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(150,     0,       -9970,   180,  389,  0x0, 0,   34,  0,   0,   0,   0,   50,  255,  0)
    DeclNpc(-1930,   0,       -10230,  270,  389,  0x0, 0,   35,  0,   0,   0,   0,   51,  255,  0)
    DeclNpc(330,     0,       -11890,  0,    389,  0x0, 0,   36,  0,   0,   0,   0,   52,  255,  0)
    DeclNpc(-1400,   0,       -11710,  45,   405,  0x0, 0,   36,  0,   0,   0,   0,   54,  255,  0)
    DeclNpc(1450,    0,       -11210,  90,   405,  0x0, 0,   35,  0,   0,   0,   0,   55,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 58,  33.0,                  0.0,                   -3.5,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.0,                 -0.0,                  0.699999988079071,     1.0])
    DeclEvent(0x0000, 0, 65,  -10.0,                 22.5,                  1.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.3333334922790527,    -2.25,                 -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  -20.0,                 -17.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0,                   5.6666669845581055,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 65,  -14.5,                 18.0,                  0.0,                   56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.9000000953674316,    -6.0,                  -0.0,                  1.0])

    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  86, 0x0000)
    DeclActor(68620,   4294964796, 15400,   1200,    68040,   4294963796, 11820,   0x007C, 0,  56, 0x0000)
    DeclActor(34000,   4294964796, 3400,    1500,    34000,   4294965796, 3400,    0x007C, 0,  57, 0x0000)
    DeclActor(77440,   4294964796, 19770,   1200,    77440,   4294966296, 19770,   0x007C, 0,  85, 0x0000)
    DeclActor(4294950666, 0,       4294960436, 1200,    4294951406, 1500,    4294961236, 0x007E, 0,  25, 0x0000)
    DeclActor(4294952406, 0,       4294958816, 1200,    4294952906, 1200,    4294959456, 0x007E, 0,  32, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Plaza")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Administrative District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential District")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown District")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Harbor District")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Alley")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "Ursula Road")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_F78",          # 00, 0
        "Function_1_1030",         # 01, 1
        "Function_2_10A5",         # 02, 2
        "Function_3_11DF",         # 03, 3
        "Function_4_120A",         # 04, 4
        "Function_5_1235",         # 05, 5
        "Function_6_12D2",         # 06, 6
        "Function_7_12FD",         # 07, 7
        "Function_8_137A",         # 08, 8
        "Function_9_13A0",         # 09, 9
        "Function_10_13CB",        # 0A, 10
        "Function_11_1D94",        # 0B, 11
        "Function_12_2021",        # 0C, 12
        "Function_13_2436",        # 0D, 13
        "Function_14_2D88",        # 0E, 14
        "Function_15_31E1",        # 0F, 15
        "Function_16_358D",        # 10, 16
        "Function_17_389C",        # 11, 17
        "Function_18_3903",        # 12, 18
        "Function_19_3D26",        # 13, 19
        "Function_20_3FC1",        # 14, 20
        "Function_21_49F6",        # 15, 21
        "Function_22_5299",        # 16, 22
        "Function_23_5A99",        # 17, 23
        "Function_24_623B",        # 18, 24
        "Function_25_682B",        # 19, 25
        "Function_26_6840",        # 1A, 26
        "Function_27_729B",        # 1B, 27
        "Function_28_739B",        # 1C, 28
        "Function_29_7437",        # 1D, 29
        "Function_30_784E",        # 1E, 30
        "Function_31_7E10",        # 1F, 31
        "Function_32_7E3C",        # 20, 32
        "Function_33_82B9",        # 21, 33
        "Function_34_910B",        # 22, 34
        "Function_35_91D2",        # 23, 35
        "Function_36_9429",        # 24, 36
        "Function_37_95B4",        # 25, 37
        "Function_38_9860",        # 26, 38
        "Function_39_9B52",        # 27, 39
        "Function_40_9CA7",        # 28, 40
        "Function_41_9EA8",        # 29, 41
        "Function_42_A0E3",        # 2A, 42
        "Function_43_A185",        # 2B, 43
        "Function_44_A233",        # 2C, 44
        "Function_45_A37B",        # 2D, 45
        "Function_46_A612",        # 2E, 46
        "Function_47_ACFC",        # 2F, 47
        "Function_48_B565",        # 30, 48
        "Function_49_BCBD",        # 31, 49
        "Function_50_BE85",        # 32, 50
        "Function_51_C19F",        # 33, 51
        "Function_52_C290",        # 34, 52
        "Function_53_C366",        # 35, 53
        "Function_54_C438",        # 36, 54
        "Function_55_C552",        # 37, 55
        "Function_56_C64F",        # 38, 56
        "Function_57_C748",        # 39, 57
        "Function_58_CFEC",        # 3A, 58
        "Function_59_DC71",        # 3B, 59
        "Function_60_FFBE",        # 3C, 60
        "Function_61_FFED",        # 3D, 61
        "Function_62_1003F",       # 3E, 62
        "Function_63_10091",       # 3F, 63
        "Function_64_100DE",       # 40, 64
        "Function_65_10172",       # 41, 65
        "Function_66_10297",       # 42, 66
        "Function_67_103BC",       # 43, 67
        "Function_68_10400",       # 44, 68
        "Function_69_10430",       # 45, 69
        "Function_70_10474",       # 46, 70
        "Function_71_104A4",       # 47, 71
        "Function_72_106CD",       # 48, 72
        "Function_73_13D68",       # 49, 73
        "Function_74_13DEF",       # 4A, 74
        "Function_75_14188",       # 4B, 75
        "Function_76_14ECA",       # 4C, 76
        "Function_77_15623",       # 4D, 77
        "Function_78_183F5",       # 4E, 78
        "Function_79_19B8D",       # 4F, 79
        "Function_80_19C91",       # 50, 80
        "Function_81_19CAD",       # 51, 81
        "Function_82_19CD0",       # 52, 82
        "Function_83_1A3E5",       # 53, 83
        "Function_84_1A9F9",       # 54, 84
        "Function_85_1AA1F",       # 55, 85
        "Function_86_1AAD5",       # 56, 86
    ))


    def Function_0_F78(): pass

    label("Function_0_F78")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_FB8"),
        (1, "loc_FC4"),
        (2, "loc_FD0"),
        (3, "loc_FDC"),
        (4, "loc_FE8"),
        (5, "loc_FF4"),
        (6, "loc_1000"),
        (SWITCH_DEFAULT, "loc_100C"),
    )


    label("loc_FB8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FC4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FD0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FDC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FE8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FF4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1000")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_100C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_102F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_102F")

    Return()

    # Function_0_F78 end

    def Function_1_1030(): pass

    label("Function_1_1030")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
    OP_95(0xFE, 17490, 0, 8720, 1000, 0x0)
    OP_95(0xFE, 17490, 0, -4030, 1000, 0x0)
    OP_95(0xFE, 12440, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, 8720, 1000, 0x0)
    Jump("Function_1_1030")

    label("loc_10A4")

    Return()

    # Function_1_1030 end

    def Function_2_10A5(): pass

    label("Function_2_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DE")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_2_10A5")

    label("loc_11DE")

    Return()

    # Function_2_10A5 end

    def Function_3_11DF(): pass

    label("Function_3_11DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1209")
    OP_94(0xFE, 0xFFFFB9BA, 0x992, 0xFFFFB118, 0xFFFFF628, 0x3E8)
    Sleep(300)
    Jump("Function_3_11DF")

    label("loc_1209")

    Return()

    # Function_3_11DF end

    def Function_4_120A(): pass

    label("Function_4_120A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1234")
    OP_94(0xFE, 0xA5FA, 0xFFFFCAA4, 0x965A, 0xFFFFB73A, 0x320)
    Sleep(700)
    Jump("Function_4_120A")

    label("loc_1234")

    Return()

    # Function_4_120A end

    def Function_5_1235(): pass

    label("Function_5_1235")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D1")
    OP_95(0xFE, -17830, 0, -4570, 1000, 0x0)
    OP_95(0xFE, -13440, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 12710, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 18920, 0, -4320, 1000, 0x0)
    OP_95(0xFE, 18920, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -13010, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -17820, 0, 4570, 1000, 0x0)
    Jump("Function_5_1235")

    label("loc_12D1")

    Return()

    # Function_5_1235 end

    def Function_6_12D2(): pass

    label("Function_6_12D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FC")
    OP_94(0xFE, 0x1F22, 0x546, 0x7D9, 0xFFFFF7FE, 0x3E8)
    Sleep(300)
    Jump("Function_6_12D2")

    label("loc_12FC")

    Return()

    # Function_6_12D2 end

    def Function_7_12FD(): pass

    label("Function_7_12FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(6000)
    Jump("Function_7_12FD")

    label("loc_1379")

    Return()

    # Function_7_12FD end

    def Function_8_137A(): pass

    label("Function_8_137A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_139F")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_8_137A")

    label("loc_139F")

    Return()

    # Function_8_137A end

    def Function_9_13A0(): pass

    label("Function_9_13A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13CA")
    OP_94(0xFE, 0xFFFFB46A, 0x730, 0xFFFFBE92, 0xFFFFFD08, 0x3E8)
    Sleep(300)
    Jump("Function_9_13A0")

    label("loc_13CA")

    Return()

    # Function_9_13A0 end

    def Function_10_13CB(): pass

    label("Function_10_13CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FD")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148D")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1460")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_147F")

    label("loc_1460")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147F")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_147F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_148D")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155C")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_154E")

    label("loc_152F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_154E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_155C")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D5")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_15F4")

    label("loc_15D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F4")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_15F4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15FD")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16B3")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x13, 1230, -690, 3680, 135)
    ClearChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x15, -18840, 0, -5150, 180)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    ClearChrFlags(0x15, 0x10)
    SetChrPos(0x21, 37750, -2500, 1640, 90)
    SetChrPos(0x22, 37750, -2500, 240, 90)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 7780, 100, -80, 270)
    Jump("loc_1D34")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1822")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x14, 0x0, 0x0)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x13, -10690, 0, -9230, 45)
    SetChrPos(0x21, 5840, 2000, 22000, 315)
    SetChrFlags(0x21, 0x10)
    SetChrPos(0x22, 5840, 2000, 23400, 270)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x24, 0x10)
    SetChrFlags(0x26, 0x10)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 1470, -700, 1200, 90)
    SetChrPos(0x2E, 4490, 2000, 23330, 90)
    SetChrPos(0x2F, 6200, -260, 2760, 135)
    SetChrPos(0x30, 4150, -700, 980, 90)
    SetChrPos(0x31, 3660, -700, -1420, 225)
    SetChrPos(0x32, 4330, 2000, 21140, 45)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2F, 0x10)
    SetChrFlags(0x30, 0x10)
    ClearChrFlags(0x31, 0x10)
    ClearChrFlags(0x32, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x13, -17390, 0, -9830, 135)
    ClearChrFlags(0x13, 0x10)

    label("loc_17FB")

    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 135)
    Jump("loc_1D34")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19D5")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x2D, 0x80)
    BeginChrThread(0x2D, 0, 0, 8)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C2")
    SetChrFlags(0x15, 0x10)
    Jump("loc_18C7")

    label("loc_18C2")

    ClearChrFlags(0x1A, 0x10)

    label("loc_18C7")

    SetChrPos(0x21, 5840, 2000, 22000, 0)
    SetChrPos(0x22, 5840, 2000, 23400, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193C")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x10)
    SetChrPos(0x16, 17000, 0, -8570, 45)
    SetChrPos(0x13, 15160, 0, -9180, 315)
    Jump("loc_19A4")

    label("loc_193C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198A")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    Jump("loc_19A4")

    label("loc_198A")

    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0x13, -18110, 0, -5400, 135)

    label("loc_19A4")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 270)
    Jump("loc_1D34")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A91")
    ClearChrFlags(0x2C, 0x80)
    BeginChrThread(0x2C, 0, 0, 7)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x21, 12500, 0, 11930, 0)
    SetChrPos(0x22, 10900, 0, 11720, 90)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x25, 0x10)
    OP_93(0x27, 0x13B, 0x0)
    SetChrFlags(0x27, 0x10)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1A, -16250, 0, -10660, 315)
    SetChrPos(0x13, -19060, 0, -5540, 0)
    SetChrPos(0x23, -14280, 0, 7050, 315)
    BeginChrThread(0x23, 0, 0, 0)
    Jump("loc_1D34")

    label("loc_1A91")

    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1D34")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2F, 0x80)
    SetChrBattleFlags(0x2F, 0x8000)
    SetChrFlags(0x30, 0x80)
    SetChrBattleFlags(0x30, 0x8000)
    SetChrFlags(0x31, 0x80)
    SetChrBattleFlags(0x31, 0x8000)
    SetChrFlags(0x32, 0x80)
    SetChrBattleFlags(0x32, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x1A, -12260, 0, -10460, 45)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -14190, 0, -10860, 45)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, -7110, 0, -9730, 45)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -7510, 0, -8540, 45)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x26, -4900, 2000, 22900, 120)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrPos(0x27, -4900, 2000, 24200, 120)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 13300, 0, 12600, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 13500, 0, 11300, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -4500, 0, 14100, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, -2700, -350, 6100, 45)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrPos(0x25, -2000, -500, 5350, 45)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_4B(0x23, 0xFF)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrPos(0x23, -3150, 0, 15000, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 2700, -400, 5500, 0)

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1D48")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 74)
    Jump("loc_1D6B")

    label("loc_1D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1D5C")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 78)
    Jump("loc_1D6B")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1D6B")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 83)

    label("loc_1D6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D93")
    SetChrPos(0x0, -19600, 0, -27950, 0)

    label("loc_1D93")

    Return()

    # Function_10_13CB end

    def Function_11_1D94(): pass

    label("Function_11_1D94")

    ClearMapObjFlags(0x4, 0x10)
    OP_66(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DC5")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE2")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1DE2")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E1A")
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_1EE6")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E28")
    Jump("loc_1EE6")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E93")
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8E")
    OP_65(0x4, 0x1)

    label("loc_1E8E")

    Jump("loc_1EE6")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EAB")
    ClearMapObjFlags(0xD, 0x4)
    OP_65(0x5, 0x1)
    Jump("loc_1EE6")

    label("loc_1EAB")

    ClearMapObjFlags(0x5, 0x4)
    OP_65(0x5, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)

    label("loc_1EE6")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 68040, -3500, 11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E1(0x13DE4, 0x0, 0x71E8)
    OP_E1(0x13C54, 0x0, 0xD1B0)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 27000, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -18500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_11_1D94 end

    def Function_12_2021(): pass

    label("Function_12_2021")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20FF")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_202D
        "You hear the news yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2049
        (
            "They're wrapping up the festivities with\x01",
            "a candy scavenger hunt today.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_20AA
        (
            "Now that's my kind of fun! You better\x01",
            "believe I'll be the first one there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_20FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_219F")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2108
        "Ugh. Those thugs are back at it again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2136
        (
            "Honestly, they're no different from a bunch of\x01",
            "toddlers, flailing and screaming for attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2221")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_21A8
        (
            "They've invited anyone to participate\x01",
            "in today's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_21EB
        "Heehee. I think I might just give it a try!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_230C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2278")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2233
        (
            "Ooh, this looks fun! I need to hurry\x01",
            "and find a good spot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2307")

    label("loc_2278")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2278
        (
            "Hmm... I can't see the stage well with\x01",
            "all of these other people around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_22C6
        (
            "I wonder if I can stake out a better spot\x01",
            "around here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2307")

    Jump("loc_2432")

    label("loc_230C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_235B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2315
        (
            "I can't wait to see what they've got in\x01",
            "store for us today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_235B")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_235B
        (
            "Yesterday's concert was absolutely amazing!\x01",
            "I've still got goosebumps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_23A7
        (
            "Honestly, they might stick around all week!\x01",
            "I'm a sucker for tourist attractions, and the\x01",
            "Anniversary Festival is here to deliver!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2432")

    TalkEnd(0xFE)
    Return()

    # Function_12_2021 end

    def Function_13_2436(): pass

    label("Function_13_2436")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D84")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        # TAG:MENU_245C
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2494")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2494")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B4")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D7F")

    label("loc_24B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C8")
    Jump("loc_2D7F")

    label("loc_24C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_261F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2543")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_24F3
        (
            "Would you all care to try my final dish\x01",
            "for the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261A")

    label("loc_2543")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2543
        (
            "Mishelam tends to get pretty crowded\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_258E
        (
            "What I wasn't expecting was for the park\x01",
            "here in the Harbor District to get so busy.\x01",
            "Looks like I've got a lot of noodles to cook. \x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_261A")

    Jump("loc_2D7F")

    label("loc_261F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2690")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2628
        (
            "This crappy song is driving away business!\x01",
            "What'd I do to deserve this? Aidios, have mercy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2BDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2780")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_26A5
        (
            "Thank Aidios! I heard the thief was caught\x01",
            "and thrown behind bars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_26ED
        (
            "Well, you know what they say: If you can't\x01",
            "do the time, don't do the crime. Maybe that'll\x01",
            "teach 'em a lesson about pulling such a stunt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD8")

    label("loc_2780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A00")

    ChrTalk(
        0x101,
        # TAG:CHRTALK_27AB
        (
            "#0000FExcuse me, could we ask you a few questions?\x02\x03",
            "We're investigating the recent string of thefts\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2821
        "Oh, yeah. I've heard about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2845
        (
            "If that conniving, little thief touches\x01",
            "MY noodles, the gloves are off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_2892
        (
            "#0003FLet's...hope it doesn't have to come to that.\x01",
            "But, while we're on the subject, could you\x01",
            "tell us what the thief looked like? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_291B
        "Hmm... What they looked like, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2943
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_294C
        (
            "Nope, I haven't got a clue. It'd be near impossible\x01",
            "to pick anyone out of these crowds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_29A9
        (
            "#0101FI know what you mean. Well, regardless,\x01",
            "thank you for your time.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xB)
    Jump("loc_2AFE")

    label("loc_2A00")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2A00
        (
            "Anyone who chooses to go on a crime spree in\x01",
            "the middle of a festival is scum, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2A63
        (
            "If that conniving, little thief touches\x01",
            "MY noodles, the gloves are off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_2AB0
        (
            "#0000F(I don't think this stall is about to be targeted\x01",
            "anytime soon...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFE")

    Jump("loc_2BD8")

    label("loc_2B03")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2B03
        (
            "There's been a string of thefts targeting\x01",
            "food stalls since yesterday. Just one person\x01",
            "after the next losing their hard-earned mira... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2B90
        (
            "This is outrageous! I'll catch the sleazeball\x01",
            "myself if I have to!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD8")

    Jump("loc_2D7F")

    label("loc_2BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CCD")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2BE6
        (
            "They say an old coot's food stall is sure to lose\x01",
            "to those fancy popcorn and gelato stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2C47
        (
            "As if that means a lick to me! I opened\x01",
            "this stall because I believe in the quality\x01",
            "of my work, and nothing'll change that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2CCD")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2CCD
        (
            "Come taste the best noodles in all of\x01",
            "Crossbell for yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2D10
        "Think I'm yanking your chain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2D33
        (
            "Just see for yourself! You won't find\x01",
            "a single noodle as good as mine!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")

    Jump("loc_2443")

    label("loc_2D84")

    TalkEnd(0xFE)
    Return()

    # Function_13_2436 end

    def Function_14_2D88(): pass

    label("Function_14_2D88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E1B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2D94
        "Lotta families out here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2DB8
        (
            "I'd bet they're all going to Mishelam,\x01",
            "seeing it's the last day of the festival\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31DD")

    label("loc_2E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2EB4")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2E2D
        (
            "There are definitely health benefits to walking,\x01",
            "I'll give it that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2E76
        "But traipsing around town gets exhausting at times.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F6C")

    label("loc_2EB4")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2EB4
        (
            "Utilizing back alleys and secret pathways in my\x01",
            "delivery route is perfect for times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2F19
        (
            "Hah! I'd like to see those bulky delivery\x01",
            "trucks try to compete with THAT.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2F6C")

    Jump("loc_31DD")

    label("loc_2F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_307A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FC3")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2F83
        "Ugh, I've gotta pick up the pace on these deliveries.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3075")

    label("loc_2FC3")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_2FC3
        (
            "Sounds like my deliveries are gonna be delayed\x01",
            "due to the traffic restrictions from the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3028
        (
            "I'm gonna have to cram in as many of them\x01",
            "as I can before it starts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3075")

    Jump("loc_31DD")

    label("loc_307A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_30F3")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_308C
        (
            "Y'know, if they've really got so much\x01",
            "steam to blow off, why don't they\x01",
            "come give ME a hand?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3161")

    label("loc_30F3")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_30F3
        (
            "There was some kind of commotion\x01",
            "at the park earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_312E
        "I guess those thugs were back at it again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3161")

    Jump("loc_31DD")

    label("loc_3166")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3166
        (
            "I can never seem to catch a break.\x01",
            "Not even for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_31B5
        "Why does this always happen to me?\x02",
    )

    CloseMessageWindow()

    label("loc_31DD")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D88 end

    def Function_15_31E1(): pass

    label("Function_15_31E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_31F6
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_31FF
        (
            "I do feel sorry for my granddaughter, but...\x01",
            "a tiger just can't change its stripes. I've got\x01",
            "no interest in all those fancy attractions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3334")

    label("loc_3292")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3292
        (
            "That damned IBC... Look what they did to my\x01",
            "fishing spot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_32D3
        (
            "I don't know anything about this 'Mishelam,'\x01",
            "but those guys are startin' to piss me off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3334")

    Jump("loc_3589")

    label("loc_3339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_33AA")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3342
        (
            "This damn racket's driving me up the wall!\x01",
            "If they don't cut it out, they're gonna regret it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_33AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_33F1")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_33B3
        (
            "Don't wanna.\x01",
            "I don't care about no stinkin' parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_33F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3483")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_33FA
        (
            "I've decided to spend the rest of my days\x01",
            "planted right here on the water I don't need\x01",
            "to go galavanting off to anywhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_3483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3512")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_348C
        (
            "Sounds like the IBC is responsible for\x01",
            "that blasted ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_34CD
        (
            "Those rat bastards, disturbing my\x01",
            "peaceful fishin' spot...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_3512")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3512
        "Aaarghhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3522
        (
            "SHADDUP ALREADY!\x01",
            "YOU'RE TOO DAMN LOUD!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_354E
        (
            "Can't you fools see I'm tryin'\x01",
            "to fish over here?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3589")

    TalkEnd(0xFE)
    Return()

    # Function_15_31E1 end

    def Function_16_358D(): pass

    label("Function_16_358D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3623")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3599
        "Mishelam sounds fun... I wish I could go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_35C8
        (
            "But there's no point in asking my grandpa\x01",
            "to come with me when he's like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_3623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3686")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_362C
        "What's with all the noise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_364C
        (
            "Looks like something's going on\x01",
            "near the stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_3686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_372B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_368F
        (
            "I heard that the parade is going to be\x01",
            "amazing this year! Everyone's telling me,\x01",
            "'You just can't miss it!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_36FF
        "You should come with me, Grandpa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_372B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_37BF")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3734
        (
            "I was really hoping I could get to\x01",
            "play with Grandpa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3771
        (
            "*sigh* I hate when he gets like this...\x01",
            "He's as stubborn as a mule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3898")

    label("loc_37BF")

    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_37C7
        "C'mon, Grandpa! Let's walk around for a bit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        # TAG:CHRTALK_37F9
        "Nope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3804
        (
            "There's this place I wanna check out.\x01",
            "Please, you gotta take me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        # TAG:CHRTALK_384A
        "Nope, not happenin'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3864
        "*siiigh* Stubborn as always...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)

    label("loc_3898")

    TalkEnd(0xFE)
    Return()

    # Function_16_358D end

    def Function_17_389C(): pass

    label("Function_17_389C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_389F
        "*click* *flash*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_38B4
        (
            "Yes! Now these photos definitely\x01",
            "capture the culture of Crossbell! ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_389C end

    def Function_18_3903(): pass

    label("Function_18_3903")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_END)), "loc_3AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D1")

    ChrTalk(
        0xD,
        # TAG:CHRTALK_3928
        (
            "#2100FOh, yeah, that reminds me. Be sure\x01",
            "to snap plenty of photos and fork 'em\x01",
            "over to me later, 'kay?\x02\x03",
            "#2109FI'm countin' on ya for some quality shots! ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_3AA4")

    label("loc_39D1")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        # TAG:CHRTALK_39D9
        (
            "#2100FNow, where was I...? Oh, yeah!\x01",
            "Time to check out all the hottest\x01",
            "spots this festival's got!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 300)

    ChrTalk(
        0xD,
        # TAG:CHRTALK_3A47
        "#2109FOff we go, Reins! Be sure to keep up!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)

    ChrTalk(
        0xE,
        # TAG:CHRTALK_3A7F
        "Y-Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 6)

    label("loc_3AA4")

    Jump("loc_3D22")

    label("loc_3AA9")


    ChrTalk(
        0xD,
        # TAG:CHRTALK_3AA9
        (
            "#2100FWell, if it isn't my favorite four!\x01",
            "Excellent work yesterday!\x02\x03",
            "#2109FI just added the finishing touches to my\x01",
            "heart-pounding article about yesterday's race!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_3B51
        "#0006FReally, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_3B6B
        (
            "#0306FWe got another article on the books, huh?\x01",
            "Can't say I didn't see that one comin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        # TAG:CHRTALK_3BC8
        (
            "#2104FYou bet'cha! We're featuring it in our extra special\x01",
            "issue set to release on the last day of the festival!\x02\x03",
            "#2100FYour little adventures always make for superb stories,\x01",
            "so I'll be keeping a close eye on you! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_3CA6
        (
            "#0006F(She's building us up just to\x01",
            "tear us down, isn't she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_3CE9
        "#0200F(That has been the pattern thus far, yes.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)

    label("loc_3D22")

    TalkEnd(0xFE)
    Return()

    # Function_18_3903 end

    def Function_19_3D26(): pass

    label("Function_19_3D26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3DB3")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3D32
        (
            "The ship to Mishelam will be arriving\x01",
            "at this dock soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3D70
        (
            "We appreciate the patience of those\x01",
            "who've been waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBD")

    label("loc_3DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3E41")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3DBC
        "*sigh* I wanna have fun with my family, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3DEE
        (
            "I think I'll submit a vacation request after\x01",
            "the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBD")

    label("loc_3E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3EC7")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3E4A
        "The ship will be departing for Mishelam shortly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3E80
        (
            "If you're looking to come aboard, we ask that\x01",
            "you do so now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBD")

    label("loc_3EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F50")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3ED0
        (
            "The ship to Mishelam will be arriving at\x01",
            "the dock in approximately five minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3F26
        "We thank you for your patience.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FBD")

    label("loc_3F50")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3F50
        "We are now boarding for the ship to Mishelam!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_3F83
        (
            "Please come forward, and be sure to\x01",
            "watch your step!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBD")

    TalkEnd(0xFE)
    Return()

    # Function_19_3D26 end

    def Function_20_3FC1(): pass

    label("Function_20_3FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FEB")
    Call(0, 82)
    Return()

    label("loc_3FEB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        # TAG:MENU_4011
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4049")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4069")
    OP_AF(0x7D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49ED")

    label("loc_4069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407D")
    Jump("loc_49ED")

    label("loc_407D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49ED")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41BB")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_40B0
        "Hey, I heard you guys caught the thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_40DF
        "Nice job! I really appreciate it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_4119
        ""
    )

    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_4123
        (
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1C6, 1)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4152
        (
            "Here, take this. Just a little something\x01",
            "to show my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_4193
        "#0100FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 1)
    Jump("loc_49ED")

    label("loc_41BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429C")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_41C5
        (
            "Heehee. Hi there. Welcome to\x01",
            "Mithra's Gelato Stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_41FE
        (
            "You won't find tastier gelato in all\x01",
            "of Zemuria! We're even the official\x01",
            "gelato of the Remiferian royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4273
        "Would you like to try some?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 4)
    Jump("loc_49ED")

    label("loc_429C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4492")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D7")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_42B0
        "Today's the last day of the Anniversary Festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_42E7
        (
            "Here's a special little something from me:\x01",
            "instructions on how to make my famous,\x01",
            "scrumptilicious gelato!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_4369
        ""
    )

    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_4373
        (
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_4397
        (
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_5A()
    OP_B0(0x13)
    Jump("loc_448D")

    label("loc_43D7")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_43D7
        "Today's the last day of the Anniversary Festival...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4410
        (
            "And as it departs, so, too, must Mithra\x01",
            "the gelato nomad... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4452
        (
            "Now's your last chance to get some,\x01",
            "so choose wisely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448D")

    Jump("loc_49ED")

    label("loc_4492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4534")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_449B
        (
            "I'd heard the parade was going to be huge,\x01",
            "but I couldn't even imagine just HOW huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_44F6
        (
            "Crossbellans sure love their spectacle,\x01",
            "don't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49ED")

    label("loc_4534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4847")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45BC")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4549
        "Anyway, the parade's going to start soon, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_457F
        "That's sure to draw in a crowd! Mira, here I come.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4842")

    label("loc_45BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465C")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_45D9
        (
            "I can't believe they pulled one over on me\x01",
            "while I was serving my customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_462B
        "How did I manage to screw up so badly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4842")

    label("loc_465C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_46EE")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4665
        (
            "Crossbell easily has the most exciting\x01",
            "festival out of anywhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_46AD
        (
            "It's a shame that all festivals must\x01",
            "come to an end...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4842")

    label("loc_46EE")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_46EE
        (
            "People all across the continent have\x01",
            "their sights set on visiting Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4740
        (
            "They'll come here and do everything\x01",
            "they've ever dreamed of, then go back\x01",
            "to their lives without skipping a beat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_47B7
        "Heehee. This really is a fascinating place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_47E8
        (
            "Out of all of my visits to Crossbell, this has\x01",
            "easily been the most exciting one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_4842")

    Jump("loc_49ED")

    label("loc_4847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_48D9")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4859
        (
            "You had it pretty hard yesterday,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_488C
        (
            "Your chivalrous deeds have spread\x01",
            "across the whole city, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4952")

    label("loc_48D9")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_48D9
        "Well, if it isn't our heroes of the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4907
        (
            "So, how 'bout it? Care for a scoop?\x01",
            "I'll even give you a discount.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_4952")

    Jump("loc_49ED")

    label("loc_4957")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4957
        (
            "You won't find tastier gelato in all\x01",
            "of Zemuria! We're even the official\x01",
            "gelato of the Remiferian royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_49CC
        "Would you like to try some?\x02",
    )

    CloseMessageWindow()

    label("loc_49ED")

    Jump("loc_3FF8")

    label("loc_49F2")

    TalkEnd(0xFE)
    Return()

    # Function_20_3FC1 end

    def Function_21_49F6(): pass

    label("Function_21_49F6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5295")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        # TAG:MENU_4A1C
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A54")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4A54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A74")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5290")

    label("loc_4A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A88")
    Jump("loc_5290")

    label("loc_4A88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5290")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4BCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4B12")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4AB3
        "You wanna try some steak?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4AD2
        (
            "The festival's almost over,\x01",
            "so why not live a little?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC6")

    label("loc_4B12")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4B12
        "It's the last day of the festival, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4B44
        (
            "I've gotta say...I'm a bit depressed\x01",
            "to see it go so soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4B84
        (
            "It almost feels like parting with a\x01",
            "friend you hold dear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_4BC6")

    Jump("loc_5290")

    label("loc_4BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4C05")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4BD4
        "Yeesh. It's so loud over by the stage.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5290")

    label("loc_4C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_518A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CAF")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4C1A
        "Hey there. Would you like to try a skewer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4C4A
        (
            "Juicy, tender steak...all on a stick for your\x01",
            "on-the go needs! I guarantee you'll love it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5185")

    label("loc_4CAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5055")

    ChrTalk(
        0x101,
        # TAG:CHRTALK_4CDA
        (
            "#0000FExcuse me, could we ask you a few questions?\x02\x03",
            "We're investigating the recent string of thefts\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4D50
        "O-Oh, yeah. That.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4D67
        (
            "Honestly, I'm not too worried over it. My sister\x01",
            "and I work this stall together, so the thief\x01",
            "would have to get through both of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4DF0
        (
            "Now, if I was just here by myself? Then I'd\x01",
            "be concerned. You can't really watch your\x01",
            "own back, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_4E60
        (
            "#0101FDo you happen to recall anyone acting\x01",
            "suspiciously around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4EAB
        "A-Actually, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4ED7
        (
            "I saw some hooligans in red tracksuits\x01",
            "come here a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_4F21
        (
            "I'd never seen those guys before, so they\x01",
            "kinda put me on edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_4F66
        "#0300FNah, those aren't the guys we're looking for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_4F9F
        (
            "#0203FI do not believe those delinquents would\x01",
            "resort to stealing.\x02\x03",
            "#0200FRegardless, do not hesitate to report any\x01",
            "issues that they may cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5034
        "S-Sure. Will do.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xC)
    Jump("loc_5107")

    label("loc_5055")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5055
        (
            "We've been so swamped with customers,\x01",
            "I haven't even had the time to catch\x01",
            "anyone acting suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_50BF
        (
            "I'll be praying to Aidios to ward\x01",
            "any thieves away from our stall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5107")

    Jump("loc_5185")

    label("loc_510C")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_510C
        "We came to Crossbell's festival from out East.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5140
        (
            "Everything's going swimmingly so far,\x01",
            "just as I hoped it would.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5185")

    Jump("loc_5290")

    label("loc_518A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5200")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5193
        "My little sister's a pro at bringing in customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_51CB
        "She's been a massive boon to our business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5290")

    label("loc_5200")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5200
        "Hey there, would you like to try a skewer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5230
        (
            "Perfectly seasoned, perfectly tender steak--\x01",
            "all on a skewer, so you can eat it on the go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5290")

    Jump("loc_4A03")

    label("loc_5295")

    TalkEnd(0xFE)
    Return()

    # Function_21_49F6 end

    def Function_22_5299(): pass

    label("Function_22_5299")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A95")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        # TAG:MENU_52BF
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_52F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5317")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A90")

    label("loc_5317")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_532B")
    Jump("loc_5A90")

    label("loc_532B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A90")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5405")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_534D
        (
            "Huh? Is that the man that's been sponsoring\x01",
            "all of these stage events?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5399
        (
            "He looks like a perfectly normal old guy...\x01",
            "I was honestly expecting someone much\x01",
            "more eccentric.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A90")

    label("loc_5405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_54FE")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_540E
        (
            "Trying to beat the heat? We've got\x01",
            "drink combos for sale today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5453
        (
            "Why don't you try one? Nothing like a nice,\x01",
            "refreshing drink to wash down a good meal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_54AF
        (
            "Come onnnn, you know you wanna!\x01",
            "Our drink combos are a bargain, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A90")

    label("loc_54FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_576C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5608")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5513
        "They managed to catch that thief, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5541
        (
            "What a relief. Now we can run our stall\x01",
            "with a little peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_558B
        (
            "There's always trouble brewing in Crossbell.\x01",
            "Letting your guard down during a festival\x01",
            "is just asking for trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5767")

    label("loc_5608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5711")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5625
        (
            "Representatives from the Business Owners' Association\x01",
            "dropped by to warn us about thieves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5685
        "I see Crossbell's still as seedy as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_56B8
        (
            "I'll be watching my stall like a hawk.\x01",
            "I can't afford to have anything stolen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5767")

    label("loc_5711")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5711
        "The police look like they're on edge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_573C
        "What's going on? Some kinda accident?\x02",
    )

    CloseMessageWindow()

    label("loc_5767")

    Jump("loc_5A90")

    label("loc_576C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5817")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_577E
        (
            "If you wanna place an order, you better\x01",
            "make it quick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_57BA
        (
            "The sun'll be setting before you know it,\x01",
            "and then where will you be? Skewer-less!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E3")

    label("loc_5817")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5817
        "Hey, you. I bet you're feeling pretty hungry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_584A
        (
            "I've got just what you need. Nothing beats\x01",
            "the taste of grilled steak on a stick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_58A1
        (
            "Go on, live a little! That's what\x01",
            "a festival's all about!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_58E3")

    Jump("loc_5A90")

    label("loc_58E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_598D")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_58F1
        (
            "You know what's the perfect festival food?\x01",
            "That's right, a skewer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5939
        (
            "Double the meat, double the fun! Come on\x01",
            "down and get some tasty skewers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A90")

    label("loc_598D")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_598D
        (
            "Nothing better than a good, old-fashioned\x01",
            "festival. I just can't give enough of 'em!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_59E7
        (
            "You know what's the perfect festival food?\x01",
            "That's right, a skewer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5A2F
        (
            "How about it, sir? I can see your mouth watering\x01",
            "at the sight of this tasty meat! Go on!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_5A90")

    Jump("loc_52A6")

    label("loc_5A95")

    TalkEnd(0xFE)
    Return()

    # Function_22_5299 end

    def Function_23_5A99(): pass

    label("Function_23_5A99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_5B3E")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5AA5
        (
            "I heard you managed to catch that thief\x01",
            "with no trouble at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5AEA
        "Hahaha! Fantastic news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5B07
        "We can finally relax and enjoy the festival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6237")

    label("loc_5B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C2B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5B47
        (
            "Mors is an incredible public speaker.\x01",
            "You give him the floor, and he works\x01",
            "magic up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5BA7
        (
            "The funny thing is, he's a whole other man\x01",
            "in the moments right before he starts.\x01",
            "Poor guy becomes a total nervous wreck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6237")

    label("loc_5C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5D26")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5C9F")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5C40
        "Huh? What are they doing on that stage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5C6D
        "All this noise is giving me a headache.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D21")

    label("loc_5C9F")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5C9F
        (
            "Wow, those bracers never cease to\x01",
            "amaze me with how quickly they work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5CEB
        (
            "Haha, now everyone's sure to enjoy\x01",
            "the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D21")

    Jump("loc_6237")

    label("loc_5D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6124")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5E08")
    OP_93(0xFE, 0x87, 0x0)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5D42
        (
            "Nothing beats the satisfaction of a long,\x01",
            "hard day's work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5D82
        (
            "Well...except maybe a nice, stiff drink!\x01",
            "Haha! You want some? It'll be my treat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_5DD8
        "You know I can't. I'm still underage!\x02",
    )

    CloseMessageWindow()
    Jump("loc_611F")

    label("loc_5E08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_5ECB")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5E15
        (
            "Nothing suspicious going on around here,\x01",
            "as far as I can tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5E59
        (
            "Hmm... We haven't figured out the thief's motives,\x01",
            "so all we can do for now is continue to make rounds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_611F")

    label("loc_5ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F83")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5EE2
        (
            "We have to alert everyone running the stalls.\x01",
            "I'd hate for anyone else to fall victim to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5F46
        "Hmm, maybe one more round would be a good idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6042")

    label("loc_5F83")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5F83
        "Back in my day, we used to fight off thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_5FB6
        (
            "But to go and ruin the whole festival just over\x01",
            "some petty cash? It makes me sick. There'll\x01",
            "be HELL to pay when we catch that scumbag!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6042")

    Jump("loc_611F")

    label("loc_6047")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6047
        (
            "That sleazeball struck again! All of Mithra's\x01",
            "hard-earned mira, gone just like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_60A1
        (
            "How is anyone supposed to enjoy the festival\x01",
            "when they have to constantly look over their\x01",
            "shoulder? It's just not right!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611F")

    Jump("loc_6237")

    label("loc_6124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_61A9")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_612D
        "Mors' granddaughter sure is a cutie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6157
        (
            "What a little ray of sunshine. I'd be\x01",
            "happy to play with her for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6237")

    label("loc_61A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61BB")
    Call(0, 33)
    Jump("loc_6237")

    label("loc_61BB")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_61BB
        "Parla used to be my idol back in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_61EA
        (
            "Hahaha! I'm still jealous Mors managed\x01",
            "to sweep her up! Damn lucky dog!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6237")

    TalkEnd(0xFE)
    Return()

    # Function_23_5A99 end

    def Function_24_623B(): pass

    label("Function_24_623B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_62D0")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6250
        (
            "Good morning, everyone! Our chairman\x01",
            "has a few words he'd like to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_62A3
        "If you would, Mr. Chairman!\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_6471")

    label("loc_62D0")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_62D0
        (
            "Well, everyone... I'm afraid I have some\x01",
            "saddening news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_630E
        (
            "This joyous festival must come to an\x01",
            "end today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_63BE
        (
            "But! We've prepared something special\x01",
            "for our final day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_63FC
        (
            "Our chairman has a few words he'd\x01",
            "like to share with you all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6446
        "If you would, Mr. Chairman!\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    SetScenarioFlags(0x1, 2)

    label("loc_6471")

    Jump("loc_6827")

    label("loc_6476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_64ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_64E5")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6488
        (
            "Whoa! What the heck are you\x01",
            "imbeciles doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_64BB
        "Get off the stage! Immediately!\x02",
    )

    CloseMessageWindow()
    Jump("loc_64E8")

    label("loc_64E5")

    Call(0, 53)

    label("loc_64E8")

    Jump("loc_6827")

    label("loc_64ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_65BB")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_64F6
        "Which team will score the most points?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6523
        (
            "Anyone's welcome to hop on stage today!\x01",
            "Go on and show us what you've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6573
        (
            "Why don't our brave folks in the audience\x01",
            "raise their hands?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_65BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6697")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_65CD
        (
            "Yesterday was a bit of a nightmare, but things\x01",
            "seem to be operating more smoothly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_662B
        (
            "Everyone's having a good time, so I think it's\x01",
            "safe to say we've moved past that little incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673C")

    label("loc_6697")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6697
        (
            "Our next street performance is bound to excite!\x01",
            "Please welcome a professional escape artist!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_66F9
        "If I could get a volunteer from the audience, please!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x14, 0x10)

    label("loc_673C")

    Jump("loc_6827")

    label("loc_6741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_67B9")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_674A
        "We still need time to prepare for the quiz tournament...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6788
        "Sit tight for a little longer, please!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_67B9")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_67B9
        (
            "Hey there! Could I ask you to wait just\x01",
            "a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_67F0
        "We're preparing for the Happy Quiz Tournament!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_6827")

    TalkEnd(0xFE)
    Return()

    # Function_24_623B end

    def Function_25_682B(): pass

    label("Function_25_682B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_683C")
    Call(0, 30)
    Jump("loc_683F")

    label("loc_683C")

    Call(0, 26)

    label("loc_683F")

    Return()

    # Function_25_682B end

    def Function_26_6840(): pass

    label("Function_26_6840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688E")
    Call(0, 77)
    Return()

    label("loc_688E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68B7")
    Call(0, 75)
    Return()

    label("loc_68B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6945")
    TalkBegin(0x15)

    ChrTalk(
        0x15,
        # TAG:CHRTALK_68C3
        "Roy and Meiling saved my hide back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_68F2
        (
            "Roy likes to pretend he's lazy, but we all know he\x01",
            "tries his hardest.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Jump("loc_729A")

    label("loc_6945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6C54")
    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A04")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_695D
        "You have my thanks, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6980
        (
            "Hmph... Those blasted thieves gave stall\x01",
            "owners a ton of grief. I should compensate\x01",
            "them, or else it wouldn't feel right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C4C")

    label("loc_6A04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6AE3")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6A11
        (
            "The Anniversary Festival usually has\x01",
            "its fair share of problems, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6A5E
        (
            "...this is unprecedented. And we're\x01",
            "helpless to do anything about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6AA9
        "I'm sorry, everyone, but we're counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C4C")

    label("loc_6AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6BDD")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6AF0
        (
            "At this rate, the stall owners may resort\x01",
            "to shutting their businesses down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6B42
        (
            "I don't want that to happen. Not after\x01",
            "everyone's waited so long for the festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6B9C
        (
            "I'm begging you. There has to be\x01",
            "something you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C4C")

    label("loc_6BDD")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6BDD
        (
            "*sigh* We've been trying our hardest\x01",
            "to warn people, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_6C1E
        "We can't tackle this problem on our own.\x02",
    )

    CloseMessageWindow()

    label("loc_6C4C")

    TalkEnd(0x15)
    Jump("loc_729A")

    label("loc_6C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6EA2")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CF1")
    Jump("loc_6D3B")

    label("loc_6CF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D11")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D3B")

    label("loc_6D11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D31")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D3B")

    label("loc_6D31")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D3B")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6E06")

    ChrTalk(
        0x15,
        # TAG:CHRTALK_6D69
        (
            "*sigh* I have to say, this year is\x01",
            "absolutely packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_6DA4
        (
            "I'm up to my neck in work. And I can only\x01",
            "chip away at it so fast as just one person...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E96")

    label("loc_6E06")


    ChrTalk(
        0x15,
        # TAG:CHRTALK_6E06
        (
            "Chairman Mors' son manages a large-scale\x01",
            "enterprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_6E40
        (
            "On the other hand, his grandson Roy has\x01",
            "rebelled against all things business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_6E96")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)
    Jump("loc_729A")

    label("loc_6EA2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F36")
    Jump("loc_6F80")

    label("loc_6F36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F56")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F80")

    label("loc_6F56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F76")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F80")

    label("loc_6F76")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F80")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70AF")

    ChrTalk(
        0x15,
        # TAG:CHRTALK_6FAF
        (
            "Hey there. Welcome to the Crossbell\x01",
            "Business Owners' Association tent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_6FFB
        (
            "Don't be afraid to come over and check\x01",
            "out what we've got here! All citizens\x01",
            "are invited to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_7069
        (
            "We also host the raffle giveaway.\x01",
            "Why not give it a try?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 5)
    Jump("loc_7293")

    label("loc_70AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_7166")

    ChrTalk(
        0x15,
        # TAG:CHRTALK_70B8
        (
            "Apparently, the heads of our organization used\x01",
            "to own street stalls themselves once upon a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_711E
        (
            "Haha. I can just imagine what they were\x01",
            "like back in the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7293")

    label("loc_7166")


    ChrTalk(
        0x15,
        # TAG:CHRTALK_7166
        (
            "Apparently, the heads of our organization used\x01",
            "to own street stalls themselves once upon a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_71CC
        (
            "I heard they used to compete with each other.\x01",
            "Feels like that's the kind of relationship most\x01",
            "people in this business have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_724D
        (
            "Haha. I can just imagine what they were\x01",
            "like back in the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_7293")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)

    label("loc_729A")

    Return()

    # Function_26_6840 end

    def Function_27_729B(): pass

    label("Function_27_729B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_729E
        "I quite enjoy the scenery around here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_72CA
        (
            "This seemed like a nice spot for a rest.\x01",
            "I'm tuckered out after looking around\x01",
            "at all the stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7331
        (
            "Once you manage to break away from the\x01",
            "crowds, Crossbell's atmosphere is actually\x01",
            "very pleasant.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_729B end

    def Function_28_739B(): pass

    label("Function_28_739B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_739E
        (
            "I guess the city and Armorica both\x01",
            "have their pros and cons...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_73E2
        (
            "Hmm... Maybe I should bring some souvenirs\x01",
            "back home for Camille and Pully.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_739B end

    def Function_29_7437(): pass

    label("Function_29_7437")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_757D")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74D5")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7454
        "You guys caught the thief already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_747C
        (
            "W-Wow... That was way faster than\x01",
            "I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_74AF
        "Phew. That's great news.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7571")

    label("loc_74D5")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_74D5
        (
            "I was worried they'd cause even more\x01",
            "damage, so this is a huge relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7521
        (
            "Now that that's settled...I guess I'd\x01",
            "better get back to manning the tent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7571")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_784A")

    label("loc_757D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_7635")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_758A
        (
            "Let's see... I think I'll go visit Mithra\x01",
            "one more time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_75C8
        (
            "It wouldn't make much sense for them\x01",
            "to hit the gelato stall AGAIN, but...I'm\x01",
            "still a bit worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_784A")

    label("loc_7635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_774E")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76FB")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7653
        "I'll keep patrolling the area.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7677
        (
            "With this thief running around, hitting one\x01",
            "stall after another, I'm sure everyone's\x01",
            "worried they're going to be next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7742")

    label("loc_76FB")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_76FB
        (
            "A simple patrol is the least I can do to\x01",
            "help ease their worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7742")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_784A")

    label("loc_774E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_784A")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7757
        (
            "Look, I'm only here 'cause Meiling said she\x01",
            "wanted to try all the festival food this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_77B7
        (
            "So, don't get it twisted! I have ZERO interest\x01",
            "in the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7810
        "Can't you tell Dad to let this go already, Grandpa?!\x02",
    )

    CloseMessageWindow()

    label("loc_784A")

    TalkEnd(0xFE)
    Return()

    # Function_29_7437 end

    def Function_30_784E(): pass

    label("Function_30_784E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A64")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78EB")
    Jump("loc_7935")

    label("loc_78EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_790B")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7935")

    label("loc_790B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_792B")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7935")

    label("loc_792B")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7935")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79AE")

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7964
        "What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7974
        "Today's your last chance to exchange prizes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7A58")

    label("loc_79AE")


    ChrTalk(
        0x17,
        # TAG:CHRTALK_79AE
        (
            "I'm only helping because they're short\x01",
            "a few pairs of hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_79F0
        (
            "Hah. Guess that goes to show how\x01",
            "easily I can be suckered into things,\x01",
            "when it comes down to it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A58")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_7E0F")

    label("loc_7A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7CCE")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B01")
    Jump("loc_7B4B")

    label("loc_7B01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B21")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B4B")

    label("loc_7B21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B41")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B4B")

    label("loc_7B41")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B4B")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BE1")

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7B7C
        "Whoa, look at all the people...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7BA1
        (
            "Maybe I should help guide them around\x01",
            "or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC2")

    label("loc_7BE1")


    ChrTalk(
        0x17,
        # TAG:CHRTALK_7BE1
        "Man, those bracers never fail to impress me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7C13
        (
            "Though, if anything's impressive today,\x01",
            "it's these massive crowds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7C5B
        (
            "You think it's 'cause of the parade?\x01",
            "Hmm... Maybe I should help guide\x01",
            "them around or something...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CC2")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_7E0F")

    label("loc_7CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7E0F")
    TalkBegin(0x17)
    SetChrSubChip(0x17, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D74")

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7CEA
        (
            "Damn it! Just thinking about it pisses me off!\x01",
            "Why should I have to help out?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7D3E
        "I want nothing to do with being a merchant!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E08")

    label("loc_7D74")


    ChrTalk(
        0x17,
        # TAG:CHRTALK_7D74
        "You guys hear about all the recent thefts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        # TAG:CHRTALK_7DA4
        (
            "I...guess I could look after things here\x01",
            "juuust in case. It feels like the least I\x01",
            "could do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E08")

    SetChrSubChip(0x17, 0x2)
    TalkEnd(0x17)

    label("loc_7E0F")

    Return()

    # Function_30_784E end

    def Function_31_7E10(): pass

    label("Function_31_7E10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7E38")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_7E1C
        "Wooow! So many stalls!\x02",
    )

    CloseMessageWindow()

    label("loc_7E38")

    TalkEnd(0xFE)
    Return()

    # Function_31_7E10 end

    def Function_32_7E3C(): pass

    label("Function_32_7E3C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7ED0")
    Jump("loc_7F1A")

    label("loc_7ED0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EF0")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F1A")

    label("loc_7EF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F10")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F1A")

    label("loc_7F10")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F1A")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7F99")

    ChrTalk(
        0x19,
        # TAG:CHRTALK_7F48
        "Hewwo, do you need any hewp?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_7F6A
        "You can exchange for pwizes with me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_82B1")

    label("loc_7F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_806F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_800D")

    ChrTalk(
        0x19,
        # TAG:CHRTALK_7FAE
        "Oooh! There was a pawade?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x19,
        # TAG:CHRTALK_7FE3
        "Heehee! That sounds weally fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_806A")

    label("loc_800D")


    ChrTalk(
        0x19,
        # TAG:CHRTALK_800D
        "Bwacers awe sooo cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_8029
        (
            "They found out who the bad guys\x01",
            "were in, like, two seconds!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_806A")

    Jump("loc_82B1")

    label("loc_806F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_82B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_81ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_8127")

    ChrTalk(
        0x19,
        # TAG:CHRTALK_8091
        "Wow, you guys awe so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_80B1
        (
            "Especiawy when those guys in unifowms came,\x01",
            "and you were like, 'Take 'em to HQ, boys!'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("loc_81E8")

    label("loc_8127")


    ChrTalk(
        0x19,
        # TAG:CHRTALK_8127
        "Wow, you guys awe so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_8147
        (
            "But the cute doggie was definitewy\x01",
            "the cooliest!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_81E8")

    Jump("loc_82B1")

    label("loc_81ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_8255")

    ChrTalk(
        0x19,
        # TAG:CHRTALK_81FA
        "I'm hewe to wook after the tent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_8220
        "If you need any hewp, just weave it to me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_82B1")

    label("loc_8255")


    ChrTalk(
        0x19,
        # TAG:CHRTALK_8255
        (
            "My bwother and I are hewping\x01",
            "out with the tent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        # TAG:CHRTALK_828A
        "Wet me know if you need anything!\x02",
    )

    CloseMessageWindow()

    label("loc_82B1")

    SetChrSubChip(0x19, 0x0)
    TalkEnd(0x19)
    Return()

    # Function_32_7E3C end

    def Function_33_82B9(): pass

    label("Function_33_82B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8307")
    Call(0, 77)
    Return()

    label("loc_8307")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8330")
    Call(0, 75)
    Return()

    label("loc_8330")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_842B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_833C
        "Phew... The festival's finally almost over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_836D
        (
            "Now, erm... Where to begin, exactly?\x01",
            "I must admit, I'm pretty hopeless when\x01",
            "it comes to introductions...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0xFE, 500)

    ChrTalk(
        0x14,
        # TAG:CHRTALK_83E6
        (
            "Just hurry up and make it\x01",
            "snappy, Mr. Chairman!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_9107")

    label("loc_842B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8677")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8485")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8440
        (
            "You troublemakers again?!\x01",
            "Cease all this violence at once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_8485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84B0")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_849A
        "Ah. Hello again.\x02",
    )

    CloseMessageWindow()

    label("loc_84B0")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_84B0
        (
            "We caught quite a lucky break thanks to\x01",
            "the bracers. They caught those rotten\x01",
            "thieves just earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_851F
        (
            "Hahaha! What a relief! We can finally\x01",
            "go back to enjoying the festival again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_866F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85CD")

    ChrTalk(
        0x101,
        # TAG:CHRTALK_8591
        "#0005F(I guess the bracers beat us to the punch.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8614")

    label("loc_85CD")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_85CD
        (
            "#0005F(Thefts...? This is the first time\x01",
            "I'm hearing about this.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8614")


    ChrTalk(
        0x104,
        # TAG:CHRTALK_8614
        (
            "#0306F(Damn it... We ended up looking like a bunch of\x01",
            "fools in front of the bracers.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_866F")

    SetScenarioFlags(0x1, 4)

    label("loc_8672")

    Jump("loc_9107")

    label("loc_8677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8D88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8739")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_868C
        (
            "Thank you for all your help, SSS.\x01",
            "Now, we can go back to enjoying\x01",
            "the festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_86E1
        (
            "Hahaha! What a relief! I'm glad to be\x01",
            "acquainted with such fine young people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D83")

    label("loc_8739")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_89D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8915")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8750
        (
            "Stalls in Central Square and the Administrative,\x01",
            "Entertainment, and Harbor Districts were targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_87B9
        (
            "It may be wise to question some of the\x01",
            "stalls that haven't been robbed, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_880B
        (
            "#0005FWe'll give it a shot. We might be able to get\x01",
            "a clearer picture that way.\x02\x03",
            "#0001FWe'll return as soon as we've finished investigating.\x01",
            "Please sit tight in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_88BF
        (
            "Will do. We'll contact you right away if\x01",
            "there are any new developments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_89D0")

    label("loc_8915")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8915
        (
            "Stalls in Central Square and the Administrative,\x01",
            "Entertainment, and Harbor Districts were targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_897E
        (
            "It may be wise to question some of the\x01",
            "stalls that haven't been robbed, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89D0")

    Jump("loc_8D83")

    label("loc_89D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_8D12")

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_89E2
        (
            "The Business Owners' Association cannot allow\x01",
            "for any more stalls to be terrorized by the thief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_8A48
        (
            "Not to mention, all this turmoil will no doubt\x01",
            "affect the customers who have come to\x01",
            "enjoy the festival if it continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_8AC6
        "Will you please apprehend the thief for us?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_8B0B
        (
            "Accept\x01",      # 0
            "Refuse\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C02")
    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 198)
    SetChrPos(0x15, -16920, 0, -9360, 198)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_0D()
    Call(0, 76)
    Return()

    label("loc_8C02")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_8C02
        (
            "#0006FSorry, but I don't think we have the time\x01",
            "right now. Our schedule is pretty packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_8C61
        "Is that so? A shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_8C7B
        (
            "Well, please come by again if you're up for\x01",
            "the task. I'd like to resolve this before the\x01",
            "thief has a chance to strike again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x1A, 0x13B, 0x0)
    OP_93(0x15, 0x87, 0x0)
    Jump("loc_8D83")

    label("loc_8D12")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8D12
        "What a mess this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8D2E
        (
            "Well, this is no time to enjoy the festival.\x01",
            "We need to resolve this, and fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D83")

    Jump("loc_9107")

    label("loc_8D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8EC4")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8D99
        "Well, if it isn't Roy. I'm surprised you've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        # TAG:CHRTALK_8DD0
        (
            "Eh, Meiling wanted me to come play with her. Do\x01",
            "me a solid and keep it a secret from my old man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8E36
        (
            "Haha, sure. I don't think he'd complain, though.\x01",
            "It IS a festival, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_8E89
        "Take the time to enjoy yourselves today.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_9107")

    label("loc_8EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_908D")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        # TAG:CHRTALK_8EE3
        "Long time no see, Parla!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        # TAG:CHRTALK_8F01
        (
            "I gotta say, if there's one thing Mors ever\x01",
            "did right, it was sweepin' you off your feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        # TAG:CHRTALK_8F60
        (
            "Who would've thought he'd manage to\x01",
            "win over our absolute idol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        # TAG:CHRTALK_8FA5
        "Oh, my. There you go with the exaggerations again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_8FDD
        (
            "I think we'd better cut you off on the booze here,\x01",
            "before you earn yourself a good smacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        # TAG:CHRTALK_903F
        "Haha, you two lovebirds never change.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_9107")

    label("loc_908D")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_908D
        (
            "Aidios... My friends are always walking\x01",
            "a fine, fine line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_90CD
        (
            "You know what'll do him some good?\x01",
            "A swift backhand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9107")

    TalkEnd(0xFE)
    Return()

    # Function_33_82B9 end

    def Function_34_910B(): pass

    label("Function_34_910B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_91CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9129")
    Call(0, 33)
    Jump("loc_91CE")

    label("loc_9129")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9129
        (
            "I'm friends with all the members of the\x01",
            "Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9174
        (
            "Haha. I swear, no matter how many\x01",
            "years go by, they're always just the same\x01",
            "as ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91CE")

    TalkEnd(0xFE)
    Return()

    # Function_34_910B end

    def Function_35_91D2(): pass

    label("Function_35_91D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_927B")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_91DE
        (
            "Welp. My kid practically begged me to take him\x01",
            "to Mishelam, and what can I say? I caved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_923C
        (
            "I think we'll spend our whole day at the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9425")

    label("loc_927B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9301")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9284
        "Oh, goodness, is that guy terrifying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_92B1
        (
            "L-Listen, son. Go on and thank the\x01",
            "gentleman so we can be on our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9425")

    label("loc_9301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9371")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_930A
        "Oh, man, the parade's gonna start soon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9337
        "I've loved these things ever since I was a kid!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9425")

    label("loc_9371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_93C1")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_937A
        (
            "Oh, wow... This Mithra is more beautiful\x01",
            "than my own wife...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9425")

    label("loc_93C1")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_93C1
        (
            "Okay, I've decided! Today's the day I'm going\x01",
            "to check out what every food stall has to offer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9425")

    TalkEnd(0xFE)
    Return()

    # Function_35_91D2 end

    def Function_36_9429(): pass

    label("Function_36_9429")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9486")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9435
        (
            "We're gonna ride a big, big boat\x01",
            "to go and visit Mishelam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9475
        "Wahoo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_95B0")

    label("loc_9486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_94D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_94C8")

    ChrTalk(
        0x22,
        # TAG:CHRTALK_9498
        "Sorry, mister! Thanks for helping me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_94CB")

    label("loc_94C8")

    Call(0, 50)

    label("loc_94CB")

    Jump("loc_95B0")

    label("loc_94D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9564")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_94D9
        "Hip hip hooray! I love festivals!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9500
        (
            "Not only that, but whenever there's a festival,\x01",
            "that means there's sure to be a parade!!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B0")

    label("loc_9564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_958A")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_956D
        "What's wrong, Dad?\x02",
    )

    CloseMessageWindow()
    Jump("loc_95B0")

    label("loc_958A")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_958A
        "Yaaay! The festival is sooo fun!\x02",
    )

    CloseMessageWindow()

    label("loc_95B0")

    TalkEnd(0xFE)
    Return()

    # Function_36_9429 end

    def Function_37_95B4(): pass

    label("Function_37_95B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9635")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_95C0
        (
            "Looks like a lot of people are heading out to\x01",
            "Mishelam today. I think I'll go with the flow\x01",
            "and join them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_985C")

    label("loc_9635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_972C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96E1")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_964A
        (
            "They managed to apprehend the thief at\x01",
            "Central Square?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9686
        (
            "What kind of a sicko would go around causing\x01",
            "so much havoc during a celebration?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9727")

    label("loc_96E1")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_96E1
        (
            "Why do all the stall owners seem so tense?\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9727")

    Jump("loc_985C")

    label("loc_972C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_97F8")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9735
        "Ice cream, juice, popcorn, and a grilled skewer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_976D
        (
            "Ahh! There's nothing better than a festival.\x01",
            "Walking down the street with everyone out\x01",
            "and celebrating puts me in a cheery mood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_985C")

    label("loc_97F8")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_97F8
        "The festival is here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9813
        (
            "Why aren't you out there having fun?\x01",
            "You've gotta enjoy yourselves!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_985C")

    TalkEnd(0xFE)
    Return()

    # Function_37_95B4 end

    def Function_38_9860(): pass

    label("Function_38_9860")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_990D")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_986C
        (
            "Don't let his appearance fool you. The chairman of\x01",
            "the Business Owners' Association is a highly capable\x01",
            "man. I'm looking forward to hearing him speak.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B4E")

    label("loc_990D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9951")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9916
        (
            "Wh-Wh-What?!\x01",
            "What's the matter with you people?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B4E")

    label("loc_9951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_99E1")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_995A
        (
            "The duo from earlier was amazing,\x01",
            "but this singer is no slouch, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_99A7
        "I can't decide who I want to give my points to!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B4E")

    label("loc_99E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9A53")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_99EA
        "Wow, that performance was incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9A15
        "They're going to rake in a ton of points, for sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B4E")

    label("loc_9A53")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9A53
        (
            "The Business Owners' Association is just\x01",
            "about to start their Happy Quiz Tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9AAD
        (
            "The grand prize is an all-expenses paid trip to Mishelam!\x01",
            "You can also win gift certificates from them as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9B22
        "This won't be one you'll want to miss!\x02",
    )

    CloseMessageWindow()

    label("loc_9B4E")

    TalkEnd(0xFE)
    Return()

    # Function_38_9860 end

    def Function_39_9B52(): pass

    label("Function_39_9B52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9B94")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9B5E
        "Ooh, it's the chairman!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9B7B
        "You can do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA3")

    label("loc_9B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9C05")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9B9D
        "Wait, what?! Aren't those the thugs from earlier?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9BD5
        "What do you guys think you're doing?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA3")

    label("loc_9C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9C55")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9C0E
        "We were told we could participate, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9C3B
        "I wanna try it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA3")

    label("loc_9C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9C77")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9C5E
        "You can do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA3")

    label("loc_9C77")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9C77
        "Don't worry, I've got this in the bag!\x02",
    )

    CloseMessageWindow()

    label("loc_9CA3")

    TalkEnd(0xFE)
    Return()

    # Function_39_9B52 end

    def Function_40_9CA7(): pass

    label("Function_40_9CA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9CDD")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9CB3
        "Aw, the festival's almost over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EA4")

    label("loc_9CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9D06")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9CE6
        "Wh-What's happening?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EA4")

    label("loc_9D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D75")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9D0F
        (
            "Boy, am I jealous... Not only is she beautiful,\x01",
            "but she also has a stunning voice to match!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EA4")

    label("loc_9D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9E5A")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9D7E
        (
            "The Business Owners' Association is\x01",
            "sponsoring today's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9DC7
        (
            "There's no way I'm missing this! Apparently,\x01",
            "all of the participants get discount coupons\x01",
            "for the food stalls, and I am HERE to collect!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EA4")

    label("loc_9E5A")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9E5A
        "Ooh, these are some great prizes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9E81
        "Sign me up! I'm raring to go!\x02",
    )

    CloseMessageWindow()

    label("loc_9EA4")

    TalkEnd(0xFE)
    Return()

    # Function_40_9CA7 end

    def Function_41_9EA8(): pass

    label("Function_41_9EA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9F29")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9EB4
        "That dude's pretty cool for an old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9EE1
        (
            "He's apparently the head of the Business\x01",
            "Owners' Association.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0DF")

    label("loc_9F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9FBC")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9F32
        (
            "All these people came outta nowhere after\x01",
            "the parade ended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9F73
        (
            "Do you think they're here because the\x01",
            "parade got them excited?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0DF")

    label("loc_9FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A039")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_9FC5
        (
            "Hmm, I still have some time until the parade starts...\x01",
            "I think I'll take a look around while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0DF")

    label("loc_A039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A078")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A042
        "Aren't you being a little too greedy, Mama?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0DF")

    label("loc_A078")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A078
        (
            "I can't wait to see what they're gonna do today!\x01",
            "I dunno how they'll top yesterday's performance!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0DF")

    TalkEnd(0xFE)
    Return()

    # Function_41_9EA8 end

    def Function_42_A0E3(): pass

    label("Function_42_A0E3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A0E6
        "At long last, it is time I depart for Mishelam. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A11E
        (
            "Granted, I've only been waiting ten minutes.\x01",
            "Doesn't mean it hasn't felt like an eternity! ㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_A0E3 end

    def Function_43_A185(): pass

    label("Function_43_A185")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A188
        (
            "Oh, man, I'm so nervous...\x01",
            "My girlfriend and I are headed to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A1D4
        (
            "It's basically become a tradition to go there\x01",
            "on the last day of the festival, right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_A185 end

    def Function_44_A233(): pass

    label("Function_44_A233")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A2A7")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A23F
        (
            "Hmm, should we bring Daddy back\x01",
            "some gelato?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A271
        "Or, no... Maybe he'd like noodles better...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A377")

    label("loc_A2A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A2F9")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A2C5
        "W-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A2D3
        "That parade was incredible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A377")

    label("loc_A2F9")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A2F9
        (
            "Me and Mommy came out to see\x01",
            "the festival today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A32F
        (
            "Heehee. I haven't got to spend this\x01",
            "much time with her in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A377")

    TalkEnd(0xFE)
    Return()

    # Function_44_A233 end

    def Function_45_A37B(): pass

    label("Function_45_A37B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A3E6")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A387
        (
            "I absolutely must bring my husband\x01",
            "home a souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A3C0
        "Hmm... What are my options?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A60E")

    label("loc_A3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A497")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A3EF
        (
            "It's a shame I couldn't see Arc en Ciel,\x01",
            "but at least I was able to enjoy the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A44A
        (
            "I'll have to invite my husband to come\x01",
            "with us next year for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A60E")

    label("loc_A497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_A4FF")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A4A0
        "Where would you like to go next, Momo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A4CC
        "Want to check out that stand over there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A60E")

    label("loc_A4FF")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A506
        (
            "My husband stayed behind to run the store\x01",
            "while Momo and I explore around the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A563
        (
            "I tried to get him to come with us, since we\x01",
            "don't get to spend much time as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A5BF
        (
            "He's not exactly the biggest fan of all this\x01",
            "commotion, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    SetScenarioFlags(0x1, 7)

    label("loc_A60E")

    TalkEnd(0xFE)
    Return()

    # Function_45_A37B end

    def Function_46_A612(): pass

    label("Function_46_A612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A7AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_A6E8")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A627
        (
            "*sigh* I've only been keeping watch of\x01",
            "the park here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A662
        (
            "It's frustrating we can't do anything about\x01",
            "what's going on at Mishelam. Even the\x01",
            "First Division has to look the other way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7AA")

    label("loc_A6E8")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A6E8
        "Tons of people are heading to Mishelam today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A71B
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_A724
        (
            "#0001F(I'd be willing to bet they know about\x01",
            "the Schwarze Auction tonight.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_A775
        "#0101F(Well, they ARE the First Division...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_A7AA")

    Jump("loc_ACF8")

    label("loc_A7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 6)), scpexpr(EXPR_END)), "loc_A9A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_A84E")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A7C1
        (
            "Don't alarm any of the citizens by letting\x01",
            "them find out that I'm acting as a guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A81B
        "Try not to speak too much to me. Thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9A0")

    label("loc_A84E")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A84E
        (
            "Don't alarm any of the citizens by letting\x01",
            "them find out that I'm acting as a guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A8A8
        "Try not to speak too much to me. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_A8D6
        (
            "#0003F(Come to think of it, I didn't even notice them\x01",
            "come in during yesterday's performance.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_A93A
        (
            "#0300F(Creepin' around kinda seems like it'd be\x01",
            "the First Division's forte, don't you think?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_A9A0")

    Jump("loc_ACF8")

    label("loc_A9A5")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_A9A5
        (
            "Oh, it's the SSS...\x01",
            "What might you all be doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_AA2B
        (
            "#0005FYou're one of the detectives from the\x01",
            "First Division, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_AA73
        (
            "#0300FYou actin' as security for the festival\x01",
            "around here or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AAC0
        (
            "Well, yes. The crowds are especially\x01",
            "vulnerable during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AB0A
        (
            "Not to mention, there are plenty of influential\x01",
            "and wealthy people here. We can't ignore\x01",
            "the possibility of a terrorist attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_AB8F
        (
            "#0100FYou must be under tremendous pressure knowing\x01",
            "the safety of these people rests in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_ABF8
        (
            "Naturally. We don't have the luxury to stand\x01",
            "around shooting the breeze like the lot of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_ACC5
        "#0200F(I am detecting hints of animosity.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 6)

    label("loc_ACF8")

    TalkEnd(0xFE)
    Return()

    # Function_46_A612 end

    def Function_47_ACFC(): pass

    label("Function_47_ACFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AE65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_AD9C")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AD11
        (
            "Not only have I learned I'm a talentless\x01",
            "hack, but now I've gone and lost my wallet!\x01",
            "This sucks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AD77
        "What the heck do I do now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE60")

    label("loc_AD9C")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AD9C
        (
            "I was thinking about going back home\x01",
            "to Liberl today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_ADDE
        "I can't seem to find my wallet anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AE0C
        (
            "What the heck do I do now?\x01",
            "Oh, Aidios...why must You\x01",
            "kick me when I'm down?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_AE60")

    Jump("loc_B561")

    label("loc_AE65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B00F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_AF1E")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AE77
        (
            "I fear I can go on no longer. Today\x01",
            "marks the end of Anton the poet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AEC3
        (
            "I haven't been here for long, but I'm considering\x01",
            "returning to Liberl already...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00A")

    label("loc_AF1E")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AF1E
        (
            "People's refusal to even acknowledge my\x01",
            "existence as I read my magnificent poetry...\x01",
            "it stings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AF83
        (
            "Am I not the creative genius I once\x01",
            "thought I was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_AFBB
        (
            "I fear I can go on no longer. Today\x01",
            "marks the end of Anton the poet...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_B00A")

    Jump("loc_B561")

    label("loc_B00F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B27A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_B0E6")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B021
        (
            "Nobody around here wants to listen to me\x01",
            "serenade their ears with my beautiful poetry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B07D
        (
            "Damn it! I'd cry tears of joy if I could get a single\x01",
            "person to stay and listen at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B275")

    label("loc_B0E6")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B0E6
        (
            "Hey, you. Care to feast your ears on the\x01",
            "poetry of a man blessed by Aidios Herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B13F
        (
            "Travel shamelessly and live with kindness...\x01",
            "The transience of the world will echo\x01",
            "through your life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B1AC
        "Well? What'd you think? Amazing, right?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_B245
        "#0003F(That was supposed to be poetry?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_B275")

    Jump("loc_B561")

    label("loc_B27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_B334")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B28C
        (
            "'In order to change one's self, the change\x01",
            "must come from within.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B2D4
        (
            "I mean, it makes sense when you say it, but...\x01",
            "how am I actually supposed to DO that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A7")

    label("loc_B334")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B334
        "I've been in Crossbell for three days now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B364
        (
            "The city rages on, but I continue to stand\x01",
            "by idly. Was I not supposed to change?!\x01",
            "Why am I still the same old Anton?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B3E0
        (
            "In the peaceful light of the ever-shining sun,\x01",
            "in the days of failure...hang in there, Anton.\x01",
            "Aidios is rooting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B45E
        (
            "Man, nothing beats a good poem.\x01",
            "That cheered me up a little bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_B4A7")

    Jump("loc_B561")

    label("loc_B4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_B55E")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B4B5
        (
            "I've got no job. No girlfriend. *sigh*\x01",
            "My life is just one big cosmic joke...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B508
        (
            "Aidios, won't you please bless me with\x01",
            "pleasant memories during my travels?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B561")

    label("loc_B55E")

    Call(0, 49)

    label("loc_B561")

    TalkEnd(0xFE)
    Return()

    # Function_47_ACFC end

    def Function_48_B565(): pass

    label("Function_48_B565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B660")
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B578
        (
            "Oh, come on, Anton. You've got to\x01",
            "stop acting like the world is ending\x01",
            "every time there's a little mishap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B5E8
        (
            "You know how it goes, anyway. Your\x01",
            "wallet's gonna pop up out of nowhere\x01",
            "after you've long forgotten about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCB9")

    label("loc_B660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_B73A")
    OP_93(0x20, 0x87, 0x0)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B679
        (
            "Hey, Anton. Check this out!\x01",
            "Doesn't this performance look fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B6BD
        (
            "Supposedly anyone can participate.\x01",
            "Wanna go and sing together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B701
        "It might lighten up that cruddy mood of yours.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B844")

    label("loc_B73A")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B73A
        (
            "Anton's been standing here all day trying to\x01",
            "read his poems to strangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B789
        (
            "It's gone about as poorly as you'd expect.\x01",
            "Poor guy's in shambles at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B7DF
        (
            "Come on, bud. Wanna check out some\x01",
            "of the food stalls? You're probably pretty\x01",
            "hungry by now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_B844")

    Jump("loc_BCB9")

    label("loc_B849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B967")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B852
        (
            "Anton came up to me this morning and said\x01",
            "that he wanted to try being a street poet all\x01",
            "of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B8BC
        (
            "This is Anton we're talking about, though.\x01",
            "Knowing him, I bet he'll give this up by\x01",
            "the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B929
        "For now, I guess I'll just roll with it like usual.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCB9")

    label("loc_B967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BBB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_BA61")
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B980
        (
            "Well, I can tell this is gonna take a while.\x01",
            "I'm sure Anton will call for me once he's\x01",
            "figured out what he wants to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_B9FD
        (
            "In the meantime, that bench is looking comfy.\x01",
            "I think I'll take myself a nice little nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBAF")

    label("loc_BA61")


    ChrTalk(
        0xFE,
        # TAG:CHRTALK_BA61
        (
            "Poor guy had his heart broken pretty badly.\x01",
            "I guess this whole poetry thing is an outlet\x01",
            "for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_BAC8
        (
            "To his credit, he's kept at it a lot longer than\x01",
            "I thought he would. Anton's a fickle guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_BB28
        (
            "Well, regardless of whether this all works out...\x01",
            "Anton hasn't taken into consideration how\x01",
            "he'll pay for his living expenses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_BBAF")

    Jump("loc_BCB9")

    label("loc_BBB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_BCA5")

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_BBBD
        (
            "We're a ways from Liberl. I've been\x01",
            "accompanying Anton here all over\x01",
            "the continent during his soul search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        # TAG:CHRTALK_BC2D
        (
            "There's never a dull moment with him around.\x01",
            "Who knows what misadventures we'll get\x01",
            "ourselves into this time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCB9")

    label("loc_BCA5")

    Call(0, 49)
    TurnDirection(0x20, 0x0, 0)
    OP_93(0x20, 0xB4, 0x0)
    SetScenarioFlags(0x2, 2)

    label("loc_BCB9")

    TalkEnd(0xFE)
    Return()

    # Function_48_B565 end

    def Function_49_BCBD(): pass

    label("Function_49_BCBD")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0x1F,
        # TAG:CHRTALK_BCD3
        (
            "I've been soul searching for a while now...\x01",
            "Pretty far away from home at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        # TAG:CHRTALK_BD2D
        (
            "I like that Crossbell is bustling all the time.\x01",
            "It makes me want to stay busy, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        # TAG:CHRTALK_BD86
        (
            "Hey, Ricky. Don't you think I'll be able\x01",
            "to figure out my life's calling in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        # TAG:CHRTALK_BDEA
        "I don't know, man. Not my place to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        # TAG:CHRTALK_BE17
        (
            "...Look. I know you've been feeling pretty\x01",
            "restless lately, but try to relax a bit, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetScenarioFlags(0x2, 1)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_49_BCBD end

    def Function_50_BE85(): pass

    label("Function_50_BE85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_BEF3")

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_BE9A
        (
            "#1601FWatch where you're goin'. Nearly drop-kicked\x01",
            "you across the damn street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C07D")

    label("loc_BEF3")

    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_BEFB
        (
            "#1601FHey, you punk. Did I say you could\x01",
            "bump into me?\x02\x03",
            "#1607FYa dropped your wallet, moron.\x01",
            "Get it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        # TAG:CHRTALK_BF6E
        "Oh, yeah. This is my wallet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        # TAG:CHRTALK_BF90
        "Sweet, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        # TAG:CHRTALK_BFA4
        "U-U-Um...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_C01E
        "#0005F(Wh-What's he doing?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_C03F
        "#0306F(Ehh... Better that we stay out of it.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)

    label("loc_C07D")

    Jump("loc_C19B")

    label("loc_C082")


    ChrTalk(
        0x2E,
        # TAG:CHRTALK_C082
        (
            "#1600FLook who it is. You mutts on the\x01",
            "job right now?\x02\x03",
            "#1602FHaha... Must suck bein' cops at a time\x01",
            "like this. Aren't we grateful for all your\x01",
            "hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_C121
        (
            "#0006F*sigh* If you actually feel bad for us, then\x01",
            "could you please not make our job any\x01",
            "harder than it needs to be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C19B")

    TalkEnd(0xFE)
    Return()

    # Function_50_BE85 end

    def Function_51_C19F(): pass

    label("Function_51_C19F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C236")

    ChrTalk(
        0x2F,
        # TAG:CHRTALK_C1AB
        (
            "Woohoo! I'm here to sing,\x01",
            "and no one's gonna stop me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        # TAG:CHRTALK_C1E6
        (
            "Yer all welcome to join in!\x01",
            "Go ahead, let it out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        # TAG:CHRTALK_C21D
        "Waaaaaahooooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C28C")

    label("loc_C236")


    ChrTalk(
        0x2F,
        # TAG:CHRTALK_C236
        "Gahahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        # TAG:CHRTALK_C247
        (
            "Would ya take a look at that?!\x01",
            "How's a squirt runnin' a stall?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C28C")

    TalkEnd(0xFE)
    Return()

    # Function_51_C19F end

    def Function_52_C290(): pass

    label("Function_52_C290")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C312")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_C30A")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x30,
        # TAG:CHRTALK_C2A9
        "If Luganov wants to sing, he's gonna sing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        # TAG:CHRTALK_C2D9
        "Just stand back and listen, idiot.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_C30D")

    label("loc_C30A")

    Call(0, 53)

    label("loc_C30D")

    Jump("loc_C362")

    label("loc_C312")


    ChrTalk(
        0x30,
        # TAG:CHRTALK_C312
        "What's with the cops lookin' all jittery?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        # TAG:CHRTALK_C341
        "Somethin' up with you guys?\x02",
    )

    CloseMessageWindow()

    label("loc_C362")

    TalkEnd(0xFE)
    Return()

    # Function_52_C290 end

    def Function_53_C366(): pass

    label("Function_53_C366")

    OP_4B(0x30, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        # TAG:CHRTALK_C36E
        (
            "Whoa! What the heck do you imbeciles\x01",
            "think you're doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        # TAG:CHRTALK_C3AD
        "Get off the stage! Now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        # TAG:CHRTALK_C3CA
        "Shut it, dumbass!\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x14, 0x30, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        # TAG:CHRTALK_C400
        "Ack! What are you doing?!\x02",
    )

    CloseMessageWindow()
    OP_64(0x14)
    OP_93(0x14, 0x0, 0x0)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x30, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_53_C366 end

    def Function_54_C438(): pass

    label("Function_54_C438")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C49A")

    ChrTalk(
        0x31,
        # TAG:CHRTALK_C444
        "I'm tellin' ya to back off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        # TAG:CHRTALK_C465
        "I'll send ya flyin' if you get in the way!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C54E")

    label("loc_C49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C4CA")

    ChrTalk(
        0x31,
        # TAG:CHRTALK_C4A3
        "Where we headed today, Wald?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C54E")

    label("loc_C4CA")


    ChrTalk(
        0x31,
        # TAG:CHRTALK_C4CA
        "You look like yer rarin' to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        # TAG:CHRTALK_C4EF
        "Where we headed today, Wald?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        # TAG:CHRTALK_C511
        (
            "Maybe we can get a sick view\x01",
            "at the top of the hill!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)

    label("loc_C54E")

    TalkEnd(0xFE)
    Return()

    # Function_54_C438 end

    def Function_55_C552(): pass

    label("Function_55_C552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C5D2")

    ChrTalk(
        0x32,
        # TAG:CHRTALK_C55E
        (
            "I bet this kid thinks he's real tough\x01",
            "bumpin' into Wald. Little punk-ass!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        # TAG:CHRTALK_C5AD
        "Does he got a death wish?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C64B")

    label("loc_C5D2")


    ChrTalk(
        0x32,
        # TAG:CHRTALK_C5D2
        (
            "Holy crap! That chick running the\x01",
            "stall is hot as hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        # TAG:CHRTALK_C60F
        (
            "Hey, honey! You wanna have a\x01",
            "good time with me later?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C64B")

    TalkEnd(0xFE)
    Return()

    # Function_55_C552 end

    def Function_56_C64F(): pass

    label("Function_56_C64F")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_C659
        (
            "#0000FThe Anniversary Festival is great,\x01",
            "but the reel party is right here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63790, 0, 7940, 1500)
    MoveCamera(45, 23, 0, 1500)
    OP_6E(280, 1500)
    SetCameraDistance(29000, 1500)
    Sleep(1000)

    SetChrName(
        # TAG:CHRNAME_C6DA
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_C6DC
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        # TAG:MENU_C6F1
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C743")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_C743")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_C64F end

    def Function_57_C748(): pass

    label("Function_57_C748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF04")
    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_C7D0
        (
            "#0100F#6PWhat should we do, Lloyd?\x02\x03",
            "Are we ready to ride the ship to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_C82B
        "#0003F#11PLet's see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_C852
        (
            "Not ready yet\x01",            # 0
            "Depart for Mishelam\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C8A3"),
        (1, "loc_CB54"),
        (SWITCH_DEFAULT, "loc_CEFF"),
    )


    label("loc_C8A3")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_C8A3
        (
            "#0000F#11PWe won't be able to take care of any further\x01",
            "support requests once we depart for Mishelam.\x02\x03",
            "The ship leaves frequently enough that we can\x01",
            "board once we're sure we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_C95F
        "#0100F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_C976
        (
            "#0202F#1PWe should take care of any shopping we need\x01",
            "and upgrade our equipment before we depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_C9DC
        (
            "#0300F#6PSounds good. We'll head back here once\x01",
            "we're all ready to roll.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_CA45
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_CA47
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you're ready to board the ship,\x01",
            "consult the schedule by the dock.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_CA97
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Additionally, any outstanding support requests\x01",
            "from the festival period will be automatically\x01",
            "terminated once you depart for Mishelam.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    EventEnd(0x5)
    Jump("loc_CEFF")

    label("loc_CB54")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_CB54
        (
            "#0000F#11POkay... Let's wait for the ship to come.\x02\x03",
            "#0006FIt might be a bit late for me to say this, but\x01",
            "does anyone else feel a little...underdressed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_CBF1
        (
            "#0106F#6PYou do have a point...\x02\x03",
            "#0108FSomething more on the formal side\x01",
            "may have been a better choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_CC5E
        (
            "#0303F#6PWell, we don't even know if they'll let us in.\x01",
            "Sure we got invites, but there's a chance\x01",
            "someone in Revache might recognize us.\x02\x03",
            "#0300FWe can at least blend in with the crowds of\x01",
            "tourists who are there for the theme park, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_CD59
        (
            "#0203F#5PEven so, I think we still stand out quite a bit.\x02\x03",
            "#0202FPerhaps I should have worn my Mishy pajamas,\x01",
            "in order to be fully incognito.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CDF1():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDF1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_CE4A
        (
            "#0012F#11PUh, no... That would just make you\x01",
            "stand out even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_CE91
        (
            "#0109F#12PIt's true that Mishy wouldn't be out of place\x01",
            "there, but still...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_65(0x0, 0x1)
    Call(0, 59)
    Jump("loc_CEFF")

    label("loc_CEFF")

    Jump("loc_CFEB")

    label("loc_CF04")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    SetChrName(
        # TAG:CHRNAME_CF11
        ""
    )

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_CF1C
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Cruise Ship Schedule\x01\x01",
            "The pride of Mishelam, Mishelam Wonderland,\x01",
            "is now open for all to enjoy! Come on down and\x01",
            "experience the greatest theme park of all time!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(-1, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_CFEB")

    Return()

    # Function_57_C748 end

    def Function_58_CFEC(): pass

    label("Function_58_CFEC")

    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_D066
        (
            "#13500085V#0008F#5PAll right, we're here.\x02\x03",
            "#13500086V#0001FLet's wait here until the next ship\x01",
            "to Mishelam arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_D0DF
        (
            "#13500087V#0100F#6PThere should be a ship every 30 minutes or so\x01",
            "at this time of day...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)

    def lambda_D148():

        label("loc_D148")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_D148")

    QueueWorkItem2(0x101, 1, lambda_D148)

    def lambda_D15A():

        label("loc_D15A")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_D15A")

    QueueWorkItem2(0x102, 1, lambda_D15A)

    def lambda_D16C():

        label("loc_D16C")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_D16C")

    QueueWorkItem2(0x104, 1, lambda_D16C)

    def lambda_D17E():
        OP_95(0xFE, 34000, -2500, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D17E)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_D19A
        (
            "#13500088V#0200F#5PApparently, the frequency is increased to once\x01",
            "every 20 minutes for the duration of the festival.\x02\x03",
            "#13500089VAccording to the schedule, the last one leaves at\x01",
            "half past midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_D265
        "#13500090V#0005F#12PWow, they operate that late?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_D2A7():
        OP_95(0xFE, 34000, -2500, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D2A7)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_D2D1():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D2D1)

    def lambda_D2DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D2DE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_D2EE
        (
            "#13500091V#0304F#6PMakes sense to me. You spend the day at the theme park\x01",
            "with a hot date, then dinner and drinks at a restaurant\x01",
            "after. It'd be pretty late by the time you get back.\x02\x03",
            "#13500092V#0300FThe hotels over there cost a pretty mira, too.\x01",
            "Ain't no way most people are coughin' up for them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        # TAG:CHRTALK_D424
        (
            "#13500093V#0106F#6PI would assume most of the hotels are\x01",
            "fully booked during the festival, anyway.\x02\x03",
            "#13500094V#0100FWhat should we do, Lloyd?\x02\x03",
            "#13500095VAre we ready to ride the ship to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_D4F4
        "#13500096V#0003F#11PLet's see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xA3, 4)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_D528
        (
            "Not ready yet\x01",            # 0
            "Depart for Mishelam\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D579"),
        (1, "loc_D865"),
        (SWITCH_DEFAULT, "loc_DC70"),
    )


    label("loc_D579")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_D579
        (
            "#13500097V#0000F#11PWe won't be able to take care of any further\x01",
            "support requests once we depart for Mishelam.\x02\x03",
            "#13500098VThe ship leaves frequently enough that we can\x01",
            "board once we're sure we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_D649
        "#13500099V#0100F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_D66A
        (
            "#13500100V#0202F#1PWe should take care of any shopping we need\x01",
            "and upgrade our equipment before we depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_D6DA
        (
            "#13500101V#0300F#6PSounds good. We'll head back here once\x01",
            "we're all ready to roll.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_D74D
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_D74F
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you're ready to board the ship,\x01",
            "consult the schedule by the dock.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_D79F
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Additionally, any outstanding support requests\x01",
            "from the festival period will be automatically\x01",
            "terminated once you depart for Mishelam.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x0, 0x1)
    EventEnd(0x5)
    Jump("loc_DC70")

    label("loc_D865")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_D865
        (
            "#13500102V#0000F#11POkay... Let's wait for the ship to come.\x02\x03",
            "#13500103V#0006FIt might be a bit late for me to say this, but\x01",
            "does anyone else feel a little...underdressed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_D916
        (
            "#13500104V#0106F#6PYou do have a point...\x02\x03",
            "#13500105V#0108FSomething more on the formal side\x01",
            "may have been a better choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_D997
        (
            "#13500106V#0303F#6PWell, we don't even know if they'll let us in.\x01",
            "Sure we got invites, but there's a chance\x01",
            "someone in Revache might recognize us.\x02\x03",
            "#13500107V#0300FWe can at least blend in with the crowds of\x01",
            "tourists who are there for the theme park, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_DAA6
        (
            "#13500108V#0203F#5PEven so, I think we still stand out quite a bit.\x02\x03",
            "#13500109V#0202FPerhaps I should have worn my Mishy pajamas,\x01",
            "in order to be fully incognito.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB52():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB52)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_DBAB
        (
            "#13500110V#0012F#11PUh, no... That would just make you\x01",
            "stand out even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_DBFC
        (
            "#13500111V#0109F#12PIt's true that Mishy wouldn't be out of place\x01",
            "there, but still...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 59)
    Jump("loc_DC70")

    label("loc_DC70")

    Return()

    # Function_58_CFEC end

    def Function_59_DC71(): pass

    label("Function_59_DC71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x32)
    LoadChrToIndex("chr/ch07300.itc", 0x33)
    SoundLoad(479)
    OP_93(0xF, 0x87, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    OP_4B(0x28, 0xFF)
    OP_4B(0x29, 0xFF)
    SetChrPos(0x21, 41400, -2500, -3400, 0)
    SetChrPos(0x22, 40300, -2500, -3400, 0)
    SetChrPos(0x28, 41400, -2500, -4700, 0)
    SetChrPos(0x29, 40300, -2500, -4700, 0)
    SetChrPos(0x101, 40300, -2500, -6000, 0)
    SetChrPos(0x102, 41400, -2500, -6000, 0)
    SetChrPos(0x103, 40300, -2500, -7300, 0)
    SetChrPos(0x104, 41400, -2500, -7300, 0)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrChipByIndex(0x44, 0xE)
    SetChrChipByIndex(0x45, 0xF)
    SetChrChipByIndex(0x46, 0x10)
    SetChrChipByIndex(0x47, 0x11)
    SetChrChipByIndex(0x48, 0x12)
    SetChrChipByIndex(0x49, 0x13)
    SetChrChipByIndex(0x4A, 0x14)
    SetChrChipByIndex(0x4B, 0x15)
    SetChrChipByIndex(0x4C, 0x16)
    SetChrChipByIndex(0x4D, 0x17)
    SetChrSubChip(0x44, 0x0)
    SetChrSubChip(0x45, 0x0)
    SetChrSubChip(0x46, 0x0)
    SetChrSubChip(0x47, 0x0)
    SetChrSubChip(0x48, 0x0)
    SetChrSubChip(0x49, 0x0)
    SetChrSubChip(0x4A, 0x0)
    SetChrSubChip(0x4B, 0x0)
    SetChrSubChip(0x4C, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x44, 0x4)
    ClearChrFlags(0x45, 0x4)
    ClearChrFlags(0x46, 0x4)
    ClearChrFlags(0x47, 0x4)
    ClearChrFlags(0x48, 0x4)
    ClearChrFlags(0x49, 0x4)
    ClearChrFlags(0x4A, 0x4)
    ClearChrFlags(0x4B, 0x4)
    ClearChrFlags(0x4C, 0x4)
    ClearChrFlags(0x4D, 0x4)
    SetChrPos(0x44, 48000, -2500, -1250, 270)
    SetChrPos(0x45, 48000, -2500, -2250, 270)
    SetChrPos(0x46, 48000, -2500, -1250, 270)
    SetChrPos(0x47, 48000, -2500, -2250, 270)
    SetChrPos(0x48, 48000, -2500, -1250, 270)
    SetChrPos(0x49, 48000, -2500, -2250, 270)
    SetChrPos(0x4A, 48000, -2500, -1250, 270)
    SetChrPos(0x4B, 48000, -2500, -2250, 270)
    SetChrPos(0x4C, 48000, -2500, -1250, 270)
    SetChrPos(0x4D, 48000, -2500, -2250, 270)
    OP_A7(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x45, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x46, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x47, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x48, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrChipByIndex(0x34, 0x32)
    SetChrSubChip(0x34, 0x0)
    SetChrPos(0x34, 33000, -2500, -1500, 90)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x80)
    ClearChrBattleFlags(0x34, 0x8000)
    SetChrChipByIndex(0x33, 0x33)
    SetChrSubChip(0x33, 0x0)
    SetChrPos(0x33, 33000, -2500, -1500, 90)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x35, 0x80)
    OP_78(0x9, 0x35)
    OP_49()
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    SetChrPos(0x35, 51800, -3850, -4000, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 512, 512, 0, 0, 512, 512, 0xFFFFFF, 0x1, "bu03500.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 512, 512, 0, 0, 512, 512, 0xFFFFFF, 0x1, "bu03400.itp")
    OP_68(35100, 1000, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(1000, 0)
    OP_68(35100, 0, -7650, 3000)
    OP_6F(0x1)
    OP_0D()

    NpcTalk(
        0x34,
        # TAG:NPCTALK_E087
        "Carefree Voice",
        "#13500112VHmm...? This where we're supposed to go?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E11E():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E11E)

    def lambda_E12B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E12B)
    Sleep(100)

    def lambda_E13B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E13B)

    def lambda_E148():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E148)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_E1C5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E1C5)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_E1DC
        "#13500113V#0005F#6P(A tourist...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_E204
        "#13500114V#0100F#12P(Likely. He's certainly dressed like one.)\x02",
    )

    CloseMessageWindow()
    OP_93(0x34, 0x2D, 0x1F4)
    Sleep(200)
    TurnDirection(0x34, 0x101, 500)
    Sleep(200)
    OP_68(39450, -1300, -5400, 2000)

    def lambda_E272():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E272)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    Sleep(200)

    NpcTalk(
        0x34,
        # TAG:NPCTALK_E290
        "Carefree Voice",
        (
            "#13500115V#3500F#5PHey there, pals.\x02\x03",
            "#13500116VMind if I ask you a quick question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_E2F7
        (
            "#13500117V#0000F#12PNo, go right ahead.\x02\x03",
            "#13500118VYou look like you're a tourist. Are you\x01",
            "looking for somewhere in particular?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x34,
        # TAG:NPCTALK_E37C
        "Carefree Voice",
        (
            "#13500119V#3506F#5PYeah, actually. This city's so big,\x01",
            "it's a little disorienting, y'know?\x02\x03",
            "#13500120V#3500FI'm trying to get to Mishelam.\x01",
            "Is this the right place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_E47F
        (
            "#13500121V#0005F#12PYeah, it sure is.\x02\x03",
            "#13500122V#0000FWe're also waiting to take the ship\x01",
            "out to Mishelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x34,
        # TAG:NPCTALK_E50D
        "Carefree Voice",
        (
            "#13500123V#3502F#5PNice, I was right on the mark.\x02\x03",
            "#13500124V#3504FSuppose I'll join you guys in line, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x34,
        # TAG:NPCTALK_E5A3
        "Carefree Voice",
        "#13500125V#3505F#5PWhoops. I haven't even introduced myself yet.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, 280, 35, 3)
    Sleep(500)

    SetChrName(
        # TAG:CHRNAME_E62A
        "Carefree Voice",
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_E63A
        (
            "#13500126VThe name's Lechter. Lechter Arundel.\x02\x03",
            "#13500127VI just got here pretty recently.\x01",
            "Took the train out from Heimdallr.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_E6EF
        "#13500128V#0005F#12PThe Imperial capital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_E71E
        "#13500129V#0100F#12POh. You're Erebonian, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_E753
        (
            "#13500130V#0300F#12PNot that often we see Imperials rockin'\x01",
            "the vacation look quite as hard as you are.\x02\x03",
            "#13500131VBetween that shirt and those shades,\x01",
            "I can tell you're a guy who's here to party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        # TAG:CHRTALK_E81D
        (
            "#13500132V#3509F#5PYeah, well, Crossbell's famous for its resort,\x01",
            "after all.\x02\x03",
            "#13500133VIt's like they say... When in Crossbell,\x01",
            "do as the Crossbellans do. I really put\x01",
            "a lot of thought into this getup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_E8ED
        (
            "#13500134V#0206F#6PMaybe you should have put a little more\x01",
            "thought elsewhere.\x02\x03",
            "#13500135V#0202FI assume you are here to visit the theme park?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x34,
        # TAG:CHRTALK_E99D
        (
            "#13500136V#3505F#5PTheme park?\x02\x03",
            "#13500137V#3501FWait, what? I didn't know they had something\x01",
            "so fun at Mishelam. Ah, man. I shoulda worn\x01",
            "my Mishy PJs instead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_EA41
        (
            "#13500138V#0012F#12PUh, yeah... I've never been to the\x01",
            "theme park, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_EA91
        (
            "#13500139V#0109F#12PMishelam began as a resort, but has\x01",
            "made a number of expansions recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        # TAG:CHRTALK_EAF4
        (
            "#13500140V#3500F#5POh? Interesting!\x02\x03",
            "#13500141V#3506FAnyway, I'm here to attend in place of my boss.\x02\x03",
            "#13500142VMaybe I shoulda done a little more research\x01",
            "before I got here, though. All that other stuff\x01",
            "sounds so fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_EC3F
        "#13500143V#0001F#12PYour...boss?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x34, 0x5A, 0x1F4)

    ChrTalk(
        0x34,
        # TAG:CHRTALK_ECD7
        "#13500144V#3502F#6POh, looks like the ship's here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_93(0xF, 0xB4, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0x35, 126220, -3850, -50690, 315)
    OP_D3(0x35, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x53, 1, 0, 64)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_EDA6():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_EDA6)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_93(0x101, 0x2D, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x103, 0x2D, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x34, 0x2D, 0x0)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x35, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_EE7E():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_EE7E)
    WaitChrThread(0x35, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x9)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    BeginChrThread(0x44, 3, 0, 60)
    Sleep(280)
    BeginChrThread(0x45, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x46, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x47, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x48, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x49, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4A, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x4B, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4C, 3, 0, 60)
    Sleep(180)
    BeginChrThread(0x4D, 3, 0, 60)
    Sleep(5000)
    BeginChrThread(0x21, 3, 0, 61)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 62)
    Sleep(800)
    BeginChrThread(0x28, 3, 0, 61)
    Sleep(200)
    BeginChrThread(0x29, 3, 0, 62)
    Sleep(2000)
    EndChrThread(0x44, 0x3)
    EndChrThread(0x45, 0x3)
    EndChrThread(0x46, 0x3)
    EndChrThread(0x47, 0x3)
    EndChrThread(0x48, 0x3)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)
    EndChrThread(0x4C, 0x3)
    EndChrThread(0x4D, 0x3)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x80)
    SetChrBattleFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x80)
    SetChrBattleFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x80)
    SetChrBattleFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x80)
    SetChrBattleFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x80)
    SetChrBattleFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x80)
    SetChrBattleFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x80)
    SetChrBattleFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x80)
    SetChrBattleFlags(0x4D, 0x8000)
    EndChrThread(0x53, 0x1)
    OP_0D()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    OP_0D()

    ChrTalk(
        0x34,
        # TAG:CHRTALK_F034
        (
            "#13500145V#3504F#6P*whistle* Now that's a boat.\x01",
            "She's a real looker, ain't she?\x02\x03",
            "#13500146V#3500FI'd better go grab myself a front-row seat\x01",
            "on the deck before they're all taken.\x02\x03",
            "#13500147V#3509FCatch you guys later! ♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x34, 3, 0, 63)
    Sleep(500)

    def lambda_F123():

        label("loc_F123")

        TurnDirection(0x101, 0x34, 300)
        Yield()
        Jump("loc_F123")

    QueueWorkItem2(0x101, 1, lambda_F123)

    def lambda_F135():

        label("loc_F135")

        TurnDirection(0x102, 0x34, 300)
        Yield()
        Jump("loc_F135")

    QueueWorkItem2(0x102, 1, lambda_F135)

    def lambda_F147():

        label("loc_F147")

        TurnDirection(0x103, 0x34, 300)
        Yield()
        Jump("loc_F147")

    QueueWorkItem2(0x103, 1, lambda_F147)

    def lambda_F159():

        label("loc_F159")

        TurnDirection(0x104, 0x34, 300)
        Yield()
        Jump("loc_F159")

    QueueWorkItem2(0x104, 1, lambda_F159)
    WaitChrThread(0x34, 3)
    SetChrFlags(0x34, 0x80)
    SetChrBattleFlags(0x34, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    WaitChrThread(0x21, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x28, 3)
    WaitChrThread(0x29, 3)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(39290, 0, -7600, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11230, 0)
    OP_0D()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_F25B
        (
            "#13500148V#0106F#5PI didn't think it was possible, but that man\x01",
            "might be even more carefree than you, Randy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_F2D4
        (
            "#13500149V#0303F#2PWhat's that supposed to mean?\x02\x03",
            "#13500150V#0301FI know I'm a player, but I ain't even close\x01",
            "to the same level as Party Boy there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_F36D
        (
            "#13500151V#0211F#6PIt's clear you underestimate just how\x01",
            "much Party Boy energy you radiate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_F3CE
        (
            "#13500152V#0012F#6PWell, it seems to me they both like a good time,\x01",
            "just in different ways.\x02\x03",
            "#13500153V#0000FRather than enjoying the nightlife and hitting on\x01",
            "women like Randy does, that Lechter guy seems\x01",
            "like he just enjoys being footloose and fancy-free.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_F4DB
        (
            "#13500154V#0309F#11PAh, you know me all too well, buddy.\x02\x03",
            "#13500155V#0300FHe looked like he was around my age, though.\x01",
            "Wonder what he's doing here all by his lonesome.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)

    NpcTalk(
        0x33,
        # TAG:NPCTALK_F592
        "Woman",
        "#13500156VOh, what a coincidence.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F60F():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F60F)

    def lambda_F61C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F61C)
    Sleep(100)

    def lambda_F62C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F62C)

    def lambda_F639():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F639)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_F6B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_F6B6)
    WaitChrThread(0x33, 1)
    TurnDirection(0x33, 0x101, 500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_F6D4
        "#13500157V#0005F#12POh, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_F6FE
        "#13500158V#0305F#12PWhoa?! Well, if it ain't my favorite gal, Kilika!\x02",
    )

    CloseMessageWindow()
    OP_68(39450, -1300, -5400, 2000)

    def lambda_F75F():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_F75F)
    WaitChrThread(0x33, 1)
    OP_6F(0x79)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(-1, 280, 35, 3)

    AnonymousTalk(
        0x33,
        # TAG:ANONTALK_F7A9
        (
            "#13500159VHaha. Thank you for your assistance the other day.\x02\x03",
            "#13500160VHave all of you gathered here to go to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x102,
        # TAG:CHRTALK_F859
        "#13500161V#0100F#12PYes, we have. How about you, Kilika?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        # TAG:CHRTALK_F897
        (
            "#13500162V#3404F#5PYes. Partly for business, but also some pleasure\x01",
            "as well.\x02\x03",
            "#13500163V#3400FMore importantly... Who was that garishly-dressed\x01",
            "gentleman you were speaking with?\x02\x03",
            "#13500164VA friend of yours, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_F975
        (
            "#13500165V#0004F#12PNope, that was our first time meeting him.\x02\x03",
            "#13500166V#0000FIt sounded like he came here from Heimdallr\x01",
            "to do some sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        # TAG:CHRTALK_FA0E
        (
            "#13500167V#3405F#5PHmm... Heimdallr...\x02\x03",
            "#13500168V#3404FHeh. I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_FA57
        "#13500169V#0005F#12P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_FA75
        "#13500170V#0205F#6PAre you acquainted with him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        # TAG:CHRTALK_FAAA
        (
            "#13500171V#3404F#5PNo. He simply had a unique air about him\x01",
            "that piqued my interest.\x02\x03",
            "#13500172V#3400FAnyway, I will be boarding now. I'd recommend\x01",
            "you do so as well, lest you miss the boat.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)

    def lambda_FBA6():

        label("loc_FBA6")

        TurnDirection(0x101, 0x33, 300)
        Yield()
        Jump("loc_FBA6")

    QueueWorkItem2(0x101, 1, lambda_FBA6)

    def lambda_FBB8():

        label("loc_FBB8")

        TurnDirection(0x102, 0x33, 300)
        Yield()
        Jump("loc_FBB8")

    QueueWorkItem2(0x102, 1, lambda_FBB8)

    def lambda_FBCA():

        label("loc_FBCA")

        TurnDirection(0x103, 0x33, 300)
        Yield()
        Jump("loc_FBCA")

    QueueWorkItem2(0x103, 1, lambda_FBCA)

    def lambda_FBDC():

        label("loc_FBDC")

        TurnDirection(0x104, 0x33, 300)
        Yield()
        Jump("loc_FBDC")

    QueueWorkItem2(0x104, 1, lambda_FBDC)
    OP_93(0x33, 0x41, 0x1F4)

    def lambda_FBF5():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_FBF5)
    WaitChrThread(0x33, 1)
    OP_93(0x33, 0x5A, 0x0)

    def lambda_FC15():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_FC15)
    Sleep(2000)

    def lambda_FC2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_FC2D)
    WaitChrThread(0x33, 1)
    WaitChrThread(0x33, 2)
    SetChrFlags(0x33, 0x80)
    SetChrBattleFlags(0x33, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_FC78
        (
            "#13500173V#0309F#12PMaaan, she's gotta be the coolest,\x01",
            "hottest chick I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_FCCA
        (
            "#13500174V#0000F#6PI know she said she was going there for\x01",
            "business, but do you guys think she's\x01",
            "headed for the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_FD4B
        (
            "#13500175V#0100F#5PConsidering she works in the entertainment\x01",
            "industry, I'd wager as much.\x02",
        )
    )

    CloseMessageWindow()
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_FE2A
        "#13500176V#0205F#12PThe ship appears to be departing soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_FE6A
        "#13500177V#0000F#6PYeah, we really should hop on.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(9210, 2000)
    OP_6F(0x10)
    OP_0D()
    OP_4C(0xF, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_71(0x9, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_FF60():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_FF60)
    WaitChrThread(0x35, 1)

    def lambda_FF7E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_FF7E)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x35, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearScenarioFlags(0x5A, 2)
    OP_24(0x1DF)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_DC71 end

    def Function_60_FFBE(): pass

    label("Function_60_FFBE")


    def lambda_FFC3():
        OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFC3)

    def lambda_FFD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFD8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_60_FFBE end

    def Function_61_FFED(): pass

    label("Function_61_FFED")


    def lambda_FFF2():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFF2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_10012():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10012)
    Sleep(3000)

    def lambda_1002A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1002A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_61_FFED end

    def Function_62_1003F(): pass

    label("Function_62_1003F")


    def lambda_10044():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10044)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_10064():
        OP_9B(0x0, 0xFE, 0x0, 0x1FA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10064)
    Sleep(3500)

    def lambda_1007C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1007C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_62_1003F end

    def Function_63_10091(): pass

    label("Function_63_10091")

    OP_95(0xFE, 42770, -2500, -2020, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_100B1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100B1)
    Sleep(1700)

    def lambda_100C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100C9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_63_10091 end

    def Function_64_100DE(): pass

    label("Function_64_100DE")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_64_100DE end

    def Function_65_10172(): pass

    label("Function_65_10172")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-13700, 3000, 22500, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -13700, 2000, 21800, 135)
    SetChrPos(0x102, -13700, 2000, 23100, 135)
    SetChrPos(0x103, -15100, 2000, 21800, 135)
    SetChrPos(0x104, -15100, 2000, 23100, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_10260
        "#13200083V#0013F#5PThat's...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_65_10172 end

    def Function_66_10297(): pass

    label("Function_66_10297")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-19100, 1500, -13300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -18400, 0, -13300, 45)
    SetChrPos(0x102, -19700, 0, -13300, 45)
    SetChrPos(0x103, -19700, 0, -14600, 45)
    SetChrPos(0x104, -18400, 0, -14600, 45)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_10385
        "#13200083V#0013F#5PThat's...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_66_10297 end

    def Function_67_103BC(): pass

    label("Function_67_103BC")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1930, 0, 14500, 4000, 0x0)
    OP_95(0xFE, 3230, 500, 17000, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_67_103BC end

    def Function_68_10400(): pass

    label("Function_68_10400")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 4400, 70, 16149, 4000, 0x0)
    TurnDirection(0xFE, 0x37, 500)
    Return()

    # Function_68_10400 end

    def Function_69_10430(): pass

    label("Function_69_10430")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1230, 0, 14880, 4000, 0x0)
    OP_95(0xFE, 2230, 200, 16400, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_69_10430 end

    def Function_70_10474(): pass

    label("Function_70_10474")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 3400, 0, 15350, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_70_10474 end

    def Function_71_104A4(): pass

    label("Function_71_104A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_106CC")

    def lambda_104B4():
        OP_9D(0xFE, 0xF14, 0x0, 0x2F58, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_104B4)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrSubChip(0x3A, 0x0)

    def lambda_104E9():
        OP_9D(0xFE, 0x17DE, 0x0, 0x2D64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_104E9)
    OP_A0(0x3A, 2000, 0x0, 0x5)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrChipByIndex(0x3F, 0x2C)
    SetChrSubChip(0x3F, 0x0)

    def lambda_1051D():
        OP_9D(0xFE, 0x1234, 0x0, 0x2E72, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_1051D)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    OP_A0(0x3F, 2000, 0x0, 0x3)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_10590():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x32, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_10590)
    OP_A0(0x3F, 2000, 0x4, 0x5)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_105BC():
        OP_A0(0x3A, 4000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_105BC)

    def lambda_105C9():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_105C9)
    OP_9D(0x3A, 0xC8A, 0x0, 0x2F58, 0x32, 0x7D0)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_10630():

        label("loc_10630")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_10630")

    QueueWorkItem2(0x3A, 2, lambda_10630)

    def lambda_1064E():

        label("loc_1064E")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_1064E")

    QueueWorkItem2(0x3F, 2, lambda_1064E)
    Sleep(1500)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_10687():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_10687)

    def lambda_106A4():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_106A4)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    Jump("Function_71_104A4")

    label("loc_106CC")

    Return()

    # Function_71_104A4 end

    def Function_72_106CD(): pass

    label("Function_72_106CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    LoadChrToIndex("chr/ch02152.itc", 0x21)
    LoadChrToIndex("chr/ch02151.itc", 0x22)
    LoadChrToIndex("chr/ch30800.itc", 0x23)
    LoadChrToIndex("chr/ch31700.itc", 0x24)
    LoadChrToIndex("chr/ch30900.itc", 0x25)
    LoadChrToIndex("chr/ch31800.itc", 0x26)
    LoadChrToIndex("chr/ch00400.itc", 0x27)
    LoadChrToIndex("chr/ch02100.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch30850.itc", 0x2A)
    LoadChrToIndex("chr/ch30950.itc", 0x2B)
    LoadChrToIndex("chr/ch30852.itc", 0x2C)
    LoadChrToIndex("chr/ch30952.itc", 0x2D)
    LoadChrToIndex("apl/ch50307.itc", 0x2E)
    LoadChrToIndex("apl/ch50309.itc", 0x2F)
    LoadChrToIndex("apl/ch50390.itc", 0x30)
    LoadChrToIndex("chr/ch00601.itc", 0x31)
    LoadChrToIndex("chr/ch00701.itc", 0x32)
    LoadEffect(0x0, "event\\eva01_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")
    LoadEffect(0x2, "battle\\cr313100.eff")
    OP_68(3210, 1480, 11840, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x38, 0x27)
    SetChrSubChip(0x38, 0x0)
    OP_90(0x38, 3200, 600, 17150, 180)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x4)
    ClearChrFlags(0x38, 0x80)
    ClearChrBattleFlags(0x38, 0x8000)
    OP_4B(0x2E, 0xFF)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    OP_90(0x2E, 5900, 800, 17600, 180)
    SetChrFlags(0x2E, 0x8000)
    ClearChrFlags(0x2E, 0x4)
    SetChrFlags(0x2E, 0x40)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrChipByIndex(0x39, 0x29)
    SetChrSubChip(0x39, 0x0)
    OP_90(0x39, 2100, 900, 17800, 180)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x80)
    ClearChrBattleFlags(0x39, 0x8000)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrPos(0x3A, 2000, 0, 12000, 90)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    ClearChrBattleFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3B, 0x26)
    SetChrSubChip(0x3B, 0x0)
    SetChrPos(0x3B, 0, 0, 13500, 135)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x80)
    ClearChrBattleFlags(0x3B, 0x8000)
    SetChrChipByIndex(0x3C, 0x25)
    SetChrSubChip(0x3C, 0x0)
    SetChrPos(0x3C, -800, 0, 10600, 90)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x80)
    ClearChrBattleFlags(0x3C, 0x8000)
    SetChrChipByIndex(0x3D, 0x25)
    SetChrSubChip(0x3D, 0x0)
    SetChrPos(0x3D, 500, 0, 9290, 45)
    SetChrFlags(0x3D, 0x8000)
    ClearChrFlags(0x3D, 0x80)
    ClearChrBattleFlags(0x3D, 0x8000)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrPos(0x3F, 5000, 0, 12000, 270)
    SetChrFlags(0x3F, 0x8000)
    ClearChrFlags(0x3F, 0x80)
    ClearChrBattleFlags(0x3F, 0x8000)
    SetChrChipByIndex(0x40, 0x24)
    SetChrSubChip(0x40, 0x0)
    SetChrPos(0x40, 8400, 0, 13500, 250)
    SetChrFlags(0x40, 0x8000)
    ClearChrFlags(0x40, 0x80)
    ClearChrBattleFlags(0x40, 0x8000)
    SetChrChipByIndex(0x41, 0x23)
    SetChrSubChip(0x41, 0x0)
    SetChrPos(0x41, 9100, 0, 11600, 270)
    SetChrFlags(0x41, 0x8000)
    ClearChrFlags(0x41, 0x80)
    ClearChrBattleFlags(0x41, 0x8000)
    SetChrChipByIndex(0x42, 0x24)
    SetChrSubChip(0x42, 0x0)
    SetChrPos(0x42, 7900, 0, 9700, 315)
    SetChrFlags(0x42, 0x8000)
    ClearChrFlags(0x42, 0x80)
    ClearChrBattleFlags(0x42, 0x8000)
    SetChrChipByIndex(0x43, 0x23)
    SetChrSubChip(0x43, 0x0)
    SetChrPos(0x43, 5100, 0, 9000, 0)
    SetChrFlags(0x43, 0x8000)
    ClearChrFlags(0x43, 0x80)
    ClearChrBattleFlags(0x43, 0x8000)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x0)
    SetChrPos(0x36, -3800, 2000, 20900, 90)
    ClearChrFlags(0x36, 0x4)
    SetChrFlags(0x36, 0x8000)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x0)
    SetChrPos(0x37, -4900, 2000, 22200, 90)
    ClearChrFlags(0x37, 0x4)
    SetChrFlags(0x37, 0x8000)
    OP_52(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Sleep(10)
    PlayBGM("ed7517", 0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x3F,
        # TAG:CHRTALK_10A55
        "#13200084V#11PGimme everything you got, ya blue bastard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        # TAG:CHRTALK_10A93
        "#13200085VI don't need you to tell me that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        # TAG:CHRTALK_10AC4
        "#13200086VLet's do this!\x02",
    )

    CloseMessageWindow()
    OP_52(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3B, 2, 0, 71)
    Sleep(3500)
    Fade(500)
    OP_68(-3180, 1310, 11540, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, -9000, 0, 11410, 90)
    SetChrPos(0x104, -9300, 0, 10010, 90)
    SetChrPos(0x102, -10000, 0, 11410, 90)
    SetChrPos(0x103, -10300, 0, 10010, 90)
    OP_0D()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_10B79
        "#13200087V#0105FHm...? What exactly are they doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_10BB2
        (
            "#13200088V#0200FI am not certain, but I do not get the impression\x01",
            "they are doing anything especially dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_10C27
        (
            "#13200089V#0305FYeah, doesn't seem like their regular\x01",
            "ol' throwdowns to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_10C78
        (
            "#13200090V#0006FWe should still ask them what's going on.\x02\x03",
            "#13200091V#0001FFortunately for us, Wazy and Wald are here,\x01",
            "so I don't think things will get out of hand...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)

    SetChrName(
        # TAG:CHRNAME_10D2D
        "Young Woman's Voice",
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_10D42
        (
            "#13200092VHey! What the heck do you guys think\x01",
            "you're doing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(5160, 940, 14220, 0)
    MoveCamera(62, 13, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    OP_68(4760, 1660, 17450, 2000)
    MoveCamera(50, 13, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(23500, 2000)
    EndChrThread(0x3B, 0xFF)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_10E89():
        OP_A0(0x3A, 5000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_10E89)

    def lambda_10E96():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_10E96)
    SetChrPos(0x3F, 3790, 0, 11880, 270)
    SetChrPos(0x3A, 2340, 0, 12120, 90)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_10F08():

        label("loc_10F08")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_10F08")

    QueueWorkItem2(0x3A, 2, lambda_10F08)

    def lambda_10F26():

        label("loc_10F26")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_10F26")

    QueueWorkItem2(0x3F, 2, lambda_10F26)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    ClearChrFlags(0x37, 0x80)
    ClearChrBattleFlags(0x37, 0x8000)

    def lambda_10F58():
        OP_95(0xFE, 4200, 2000, 20900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_10F58)
    Sleep(50)

    def lambda_10F75():
        OP_95(0xFE, 3400, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_10F75)
    WaitChrThread(0x36, 1)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)

    def lambda_10F9B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x36, 2, lambda_10F9B)
    WaitChrThread(0x37, 1)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)

    def lambda_10FB4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x37, 2, lambda_10FB4)

    def lambda_10FC1():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_10FC1)
    Sleep(50)

    def lambda_10FD1():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_10FD1)
    Sleep(50)
    TurnDirection(0x39, 0x36, 500)
    OP_0D()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_10FE4
        "#13200093V#1605F#12PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_11002
        "#13200094V#0405F#12POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_1101F
        (
            "#13200095V#0806FWe got a call about some hooligans causing\x01",
            "problems, so we came here as fast as we could...\x02\x03",
            "#13200096V#0801FAren't you those Testaments and Saber Viper guys\x01",
            "from the Downtown District?\x02\x03",
            "#13200097VYou better stop all this fighting and scram, pronto!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_1114B():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_1114B)

    def lambda_11168():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_11168)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x3A, 0)
    WaitChrThread(0x3F, 0)

    def lambda_11195():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_11195)

    def lambda_111A2():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x40, 0, lambda_111A2)

    def lambda_111AF():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x41, 0, lambda_111AF)

    def lambda_111BC():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_111BC)

    def lambda_111C9():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x43, 0, lambda_111C9)

    def lambda_111D6():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_111D6)

    def lambda_111E3():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3B, 0, lambda_111E3)

    def lambda_111F0():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3C, 0, lambda_111F0)

    def lambda_111FD():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3D, 0, lambda_111FD)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_11205
        "#13200098V#1601F#12PThe hell's up with this chick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_1123D
        (
            "#13200099V#0903FPardon us. We're with the Bracer Guild.\x02\x03",
            "#13200100V#0901FWe received a message claiming that a fight\x01",
            "had broken out, so we're here to intervene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x3F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x41, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x40, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(4440, 2550, 18850, 2000)
    MoveCamera(37, 13, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(23630, 2000)
    Sleep(2000)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_1139C
        "#13200101V#1605F#12PThe guild?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_113C1
        (
            "#13200102V#0404F#6P#NYou're Joshua and Estelle Bright...\x02\x03",
            "#13200103V#0400FYour faces have been all over the\x01",
            "magazines recently.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_11447
        (
            "#13200104V#0806F#5PYeah, yeah. The pleasure's all mine.\x02\x03",
            "#13200105V#0800FYou two are the leaders of these goons, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_114C4
        (
            "#13200106V#0404F#6P#NI suppose you could call us that.\x02\x03",
            "#13200107V#0400FI'm Wazy, leader of the Testaments, and this\x01",
            "here is Wald, leader of the Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_11569
        (
            "#13200108V#0903F#5PThat matches the contents of the report.\x02\x03",
            "#13200109V#0900FIt doesn't look like you guys are having a\x01",
            "serious fight, so what exactly are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_11614
        (
            "#13200110V#0404F#6P#NOh, don't mind us. We're just having a bit of fun.\x02\x03",
            "#13200111VSeeing as how it's the Anniversary Festival,\x01",
            "we thought we'd try something a little different\x01",
            "from the usual routine.\x02\x03",
            "#13200112V#0402FAnd so, we're having ourselves a series of\x01",
            "one-on-one battles to decide which side\x01",
            "is victorious.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_11756
        (
            "#13200113V#0805F#5PA series of battles? What are you guys\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x39, 0x36, 500)

    ChrTalk(
        0x39,
        # TAG:CHRTALK_117AB
        (
            "#13200114V#4100F#6PBoth teams have nominated five members\x01",
            "each to engage in one-on-one battles.\x02\x03",
            "#13200115V#4100F#6PThe final match will be between Wazy and Wald.\x02\x03",
            "#13200116V#4100F#6PWe've agreed that the losing side will cover\x01",
            "the winners' meal expenses for the remainder\x01",
            "of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_118C8
        (
            "#13200117V#0805F#5POh, that makes perfect sense! You guys are just\x01",
            "having a friendly exhibition match.\x02\x03",
            "#13200118V#0809FThat sounds fun, so I guess I can let it slide--\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x36,
        # TAG:CHRTALK_119A4
        (
            "#13200119V#0806F#5PAs if!\x02\x03",
            "#13200120V#0801FI don't care if it's a friendly match. That\x01",
            "doesn't make it okay to do it out here!\x02\x03",
            "#13200121VMove your butts somewhere else! A lot of\x01",
            "people pass through this street and you're\x01",
            "being a total nuisance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_11A9F
        (
            "#13200122V#1603F#12PHah! Fat chance!\x02\x03",
            "#13200123V#1601FYou know... I don't give a damn if you're bracers\x01",
            "or whatever, but what does piss me off is how\x01",
            "you keep acting like you're hot shit!\x02\x03",
            "#13200124VDon't get so damn cocky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_11B84
        (
            "#13200125V#0803F#5PNow you listen here, bub...\x01",
            "You're the idiot who's too cocky!\x02\x03",
            "#13200126V#0801FAll I'm telling you to do is have\x01",
            "some common courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_11C23
        "#13200127V#1600F#12PYou bitch...\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x0, 0x1F4)
    OP_68(5860, 2550, 20980, 2000)

    def lambda_11C66():

        label("loc_11C66")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_11C66")

    QueueWorkItem2(0x36, 2, lambda_11C66)

    def lambda_11C78():

        label("loc_11C78")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_11C78")

    QueueWorkItem2(0x37, 2, lambda_11C78)
    OP_95(0x2E, 6200, 2000, 20800, 2000, 0x0)
    TurnDirection(0x2E, 0x36, 500)
    EndChrThread(0x36, 0x2)
    EndChrThread(0x37, 0x2)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_11CA8
        (
            "#13200128V#1604F#11PSounds like you're asking to get your ass kicked.\x02\x03",
            "#13200129V#1602FI don't mind taking you and your little friend on,\x01",
            "if that's what'cha want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_11D50
        (
            "#13200130V#0806F#6PW-Well...\x02\x03",
            "#13200131V#0808FHow should we handle this, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_11DA6
        (
            "#13200132V#0903F#5PHmm... Everybody's watching us now.\x02\x03",
            "#13200133V#0900FDon't make any rash decisions. It'd reflect\x01",
            "poorly on the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_11E34
        "#13200134V#0802F#6PYeah, I figured as much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_11E93
        (
            "#13200135V#1607F#11PWhat the hell are you guys whisperin'\x01",
            "about over there?!\x02\x03",
            "#13200136VOh, I get it. You're gettin' ready to piss\x01",
            "yourselves, now that you gotta face\x01",
            "Wald Wales, the Demon Smasher!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6010, 2550, 21180, 800)
    SetCameraDistance(23800, 800)
    OP_95(0x38, 3500, 1100, 18200, 1800, 0x0)
    TurnDirection(0x38, 0x2E, 500)
    OP_6F(0x1)

    ChrTalk(
        0x38,
        # TAG:CHRTALK_11F95
        (
            "#13200137V#0406F#6P#NSettle down, Wald.\x02\x03",
            "#13200138V#0400FShe definitely knows her way around a fight.\x01",
            "In fact, I'd say odds are good she'd take you\x01",
            "down without breaking a sweat.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2E, 0x38, 500)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_12071
        "#13200139V#1605F#11PWhat'd you say?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x36, 0x38, 500)
    Sleep(150)

    ChrTalk(
        0x36,
        # TAG:CHRTALK_120A5
        "#13200140V#0800F#5POh? How'd you know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x38, 0x36, 500)
    Sleep(150)

    ChrTalk(
        0x38,
        # TAG:CHRTALK_120DB
        (
            "#13200141V#0404F#12P#NIt was just a hunch.\x02\x03",
            "#13200142V#0402FLet's not ignore your friend over there, either.\x01",
            "He's even stronger than you, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x38, 500)
    Sleep(150)

    ChrTalk(
        0x37,
        # TAG:CHRTALK_1217E
        (
            "#13200143V#0902F#5PHaha... I've still got a lot of training\x01",
            "ahead of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_121CC
        (
            "#13200144V#0806F#5PHey! Rude! I mean, sure, Joshua IS stronger\x01",
            "than me...\x02\x03",
            "#13200145V#0801F...but it still pisses me off that you'd just\x01",
            "assume that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_12267
        (
            "#13200146V#0904F#5PNow, now. You know that being a bracer comes\x01",
            "down to more than just brute strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    TurnDirection(0x2E, 0x36, 500)
    Sleep(1000)
    Sound(1807, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_12302
        (
            "#13200147V#1602F#11PHaha... You're tellin' me this girlie\x01",
            "could beat me in a fight?\x02\x03",
            "#13200148V#1607FHA! You think you're so tough?\x01",
            "Prove it!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5680, 2550, 20990, 1000)
    SetCameraDistance(21320, 1000)

    def lambda_123B4():

        label("loc_123B4")

        TurnDirection(0xFE, 0x2E, 600)
        Yield()
        Jump("loc_123B4")

    QueueWorkItem2(0x36, 0, lambda_123B4)
    OP_99(0x2E, 0x36, 0x3E8, 0xBB8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x2E)
    SetChrSubChip(0x2E, 0x0)
    SetChrFlags(0x2E, 0x20)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x37,
        # TAG:CHRTALK_123EC
        "#13200149V#0901F#5PYou got this, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_1241B
        "#13200150V#0804F#6PYup! It'll be a piece of cake!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(4190, 2920, 19620, 0)
    MoveCamera(359, 8, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(25000, 1000)
    SetChrChipByIndex(0x3F, 0x23)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x25)
    SetChrSubChip(0x3A, 0x0)
    OP_93(0x36, 0x5A, 0x0)

    def lambda_124B8():

        label("loc_124B8")

        TurnDirection(0xFE, 0x2E, 300)
        Yield()
        Jump("loc_124B8")

    QueueWorkItem2(0x37, 0, lambda_124B8)
    SetChrChipByIndex(0x2E, 0x30)
    SetChrSubChip(0x2E, 0x0)
    SetChrPos(0x2E, 5300, 2300, 20900, 270)
    Sound(804, 0, 100, 0)
    OP_D3(0x2E, 0x0, 0x0, 0x15F90, 0x0)
    Sound(1648, 255, 100, 0)
    Sound(534, 0, 100, 0)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x2E, 0x100)

    def lambda_12518():
        OP_9D(0xFE, 0x9C4, 0x7D0, 0x526C, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_12518)
    OP_D3(0x2E, 0x0, 0x0, 0x57E40, 0x384)
    SetChrChipByIndex(0x2E, 0x2F)
    SetChrSubChip(0x2E, 0x0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sound(819, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_9D(0x2E, 0x7D0, 0x7D0, 0x5334, 0x190, 0x7D0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x64, 0x5DC, 0x96)
    Sound(819, 0, 100, 0)
    CancelBlur(0)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x2E, 0x1)
    Sleep(500)
    EndChrThread(0x37, 0x0)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_12622
        "#13200152V#1605F#11PWha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_12641
        "#13200153V#0406F#6PWhat did I tell you?\x02",
    )

    CloseMessageWindow()
    OP_68(4320, 2270, 18840, 3000)
    MoveCamera(359, 7, 0, 3000)
    OP_6E(380, 3000)
    SetCameraDistance(25000, 3000)
    OP_63(0x3F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x40, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x41, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x3F)
    OP_64(0x40)
    OP_64(0x41)
    OP_64(0x3A)
    OP_64(0x3B)
    OP_64(0x3C)

    ChrTalk(
        0x40,
        # TAG:CHRTALK_1271D
        "#13200154V#11PSh-She took down Wald?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        # TAG:CHRTALK_12748
        "#13200155V#5PWhat the hell's up with that chick?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3B,
        # TAG:CHRTALK_1277F
        "#13200156V#5PThat was amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        # TAG:CHRTALK_127A3
        "#13200157V#5PAre all bracers this strong?!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2720, 2400, 21470, 0)
    MoveCamera(336, 12, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_63(0x2E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2E)

    ChrTalk(
        0x36,
        # TAG:CHRTALK_1281E
        "#13200158V#0805F#12PHey there, buddy. You all right?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x2E, 0x2)

    def lambda_12866():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_12866)
    WaitChrThread(0x2E, 2)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_1287E
        "#13200159V#1604F#11PHahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_128A9():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_128A9)
    SetChrSubChip(0x2E, 0x1)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_128D5
        "#13200160V#1609F#4S#11P#NHAHAHAHAHAHA!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2450, 2500, 22450, 800)
    SetCameraDistance(26180, 800)
    Sound(804, 0, 100, 0)
    Sound(534, 0, 100, 0)
    SetChrFlags(0x2E, 0x100)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)

    def lambda_12941():
        TurnDirection(0xFE, 0x36, 800)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_12941)
    OP_9C(0x2E, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x2E, 0x1)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_12971
        (
            "#13200161V#1604F#5PMy bad. I wasn't takin' you seriously.\x02\x03",
            "#13200162V#1601FDon't you think yer takin' me a little\x01",
            "too lightly, yourself, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_12A07
        "#13200163V#0801F#12P...!\x02",
    )

    CloseMessageWindow()
    OP_68(3100, 2500, 22470, 800)
    SetCameraDistance(24870, 800)
    BeginChrThread(0x36, 3, 0, 73)
    SetChrChipByIndex(0x2E, 0x21)
    SetChrSubChip(0x2E, 0x0)
    Sleep(90)
    SetChrSubChip(0x2E, 0x1)
    Sleep(90)
    SetChrSubChip(0x2E, 0x2)
    Sleep(90)

    def lambda_12A63():

        label("loc_12A63")

        TurnDirection(0xFE, 0x36, 100)
        Yield()
        Jump("loc_12A63")

    QueueWorkItem2(0x37, 2, lambda_12A63)
    SetChrFlags(0x2E, 0x20)
    Sound(1789, 255, 100, 0)
    Sound(532, 0, 100, 0)

    def lambda_12A8A():
        OP_96(0xFE, 0xAF0, 0x7D0, 0x529E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_12A8A)
    SetChrSubChip(0x2E, 0x3)
    Sleep(70)
    SetChrSubChip(0x2E, 0x4)
    WaitChrThread(0x2E, 1)
    SetChrSubChip(0x2E, 0x5)
    ClearChrFlags(0x2E, 0x20)
    PlayEffect(0x2, 0xFF, 0x2E, 0x140, 0, 100, 1300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    Sound(895, 0, 100, 0)
    Sound(834, 0, 100, 0)
    Sleep(800)
    WaitChrThread(0x36, 3)
    Sleep(500)

    ChrTalk(
        0x36,
        # TAG:CHRTALK_12B19
        "#13200165V#0807F#12PWh-Whoa! That was close!\x02",
    )

    CloseMessageWindow()
    Sound(1780, 255, 100, 0)

    ChrTalk(
        0x37,
        # TAG:CHRTALK_12B53
        "#13200166V#0901F#5PEstelle!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x37, 0x2)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x3)

    def lambda_12B85():
        OP_9D(0xFE, 0x157C, 0x7D0, 0x5078, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_12B85)
    Sound(814, 0, 100, 0)

    def lambda_12BAA():

        label("loc_12BAA")

        TurnDirection(0xFE, 0x2E, 1000)
        Yield()
        Jump("loc_12BAA")

    QueueWorkItem2(0x37, 2, lambda_12BAA)
    WaitChrThread(0x37, 0)
    PlayEffect(0x1, 0xFF, 0x37, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)
    Sleep(100)
    OP_95(0x38, 3150, 1600, 19150, 2000, 0x0)
    TurnDirection(0x38, 0x37, 500)
    EndChrThread(0x37, 0x2)

    ChrTalk(
        0x38,
        # TAG:CHRTALK_12C1C
        (
            "#13200167V#0404F#6PSheesh...\x02\x03",
            "#13200168V#0400FYou guys asked for this, you know?\x01",
            "Don't start a fight with him if you're\x01",
            "not going to finish it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_12CB1
        (
            "#13200169V#0903F#11PYeah, I get it.\x02\x03",
            "#13200170V#0901FBut I don't really feel like we should\x01",
            "have to be the ones to apologize here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x6)
    Sleep(90)
    SetChrSubChip(0x2E, 0x7)
    Sleep(90)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_12D5D
        (
            "#13200171V#1602F#5PHaha... Got you all riled up, didn't I?\x02\x03",
            "#13200172V#1604FYou're a hell of a fighter. I can tell.\x02\x03",
            "#13200173V#1601FI love beatin' the piss out of guys like you\x01",
            "more than anythin' else!\x02\x03",
            "#13200174VCome on! Pull out that weapon of yours, punk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_12E66
        "#13200175V#0901F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_12E83
        (
            "#13200176V#0801F#12PH-Hey! Cool your jets, Joshua!\x02\x03",
            "#13200177VI'm fine. You don't need to get all serious!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1086, 255, 100, 0)

    NpcTalk(
        0x101,
        # TAG:NPCTALK_12EFE
        "Lloyd",
        "#13200178VHold it right there!\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x38, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(20, 1750, 13750, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -2450, 0, 13210, 90)
    SetChrPos(0x104, -2720, 0, 11440, 90)
    SetChrPos(0x102, -4470, 0, 12520, 90)
    SetChrPos(0x103, -4720, 0, 10900, 90)
    BeginChrThread(0x101, 0, 0, 67)
    BeginChrThread(0x104, 0, 0, 68)
    BeginChrThread(0x102, 0, 0, 69)
    BeginChrThread(0x103, 0, 0, 70)

    def lambda_13030():

        label("loc_13030")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_13030")

    QueueWorkItem2(0x36, 0, lambda_13030)

    def lambda_13042():

        label("loc_13042")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_13042")

    QueueWorkItem2(0x37, 0, lambda_13042)

    def lambda_13054():

        label("loc_13054")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_13054")

    QueueWorkItem2(0x38, 0, lambda_13054)

    def lambda_13066():

        label("loc_13066")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_13066")

    QueueWorkItem2(0x2E, 0, lambda_13066)

    def lambda_13078():

        label("loc_13078")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_13078")

    QueueWorkItem2(0x39, 0, lambda_13078)

    def lambda_1308A():

        label("loc_1308A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1308A")

    QueueWorkItem2(0x3F, 0, lambda_1308A)

    def lambda_1309C():

        label("loc_1309C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1309C")

    QueueWorkItem2(0x40, 0, lambda_1309C)

    def lambda_130AE():

        label("loc_130AE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_130AE")

    QueueWorkItem2(0x41, 0, lambda_130AE)

    def lambda_130C0():

        label("loc_130C0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_130C0")

    QueueWorkItem2(0x42, 0, lambda_130C0)

    def lambda_130D2():

        label("loc_130D2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_130D2")

    QueueWorkItem2(0x43, 0, lambda_130D2)

    def lambda_130E4():

        label("loc_130E4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_130E4")

    QueueWorkItem2(0x3A, 0, lambda_130E4)

    def lambda_130F6():

        label("loc_130F6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_130F6")

    QueueWorkItem2(0x3B, 0, lambda_130F6)

    def lambda_13108():

        label("loc_13108")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_13108")

    QueueWorkItem2(0x3C, 0, lambda_13108)
    OP_68(4220, 2200, 18860, 4000)
    MoveCamera(328, 17, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(26000, 4000)
    WaitChrThread(0x101, 0)
    EndChrThread(0x36, 0x0)
    EndChrThread(0x37, 0x0)
    EndChrThread(0x38, 0x0)
    EndChrThread(0x2E, 0x0)
    EndChrThread(0x39, 0x0)

    ChrTalk(
        0x38,
        # TAG:CHRTALK_1315B
        "#13200179V#0405F#11PWell, if it isn't the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_1318F
        "#13200180V#0805F#11PWhat are you guys doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_131C6
        (
            "#13200181V#0003F#6PWe saw the whole thing go down.\x02\x03",
            "#13200182V#0001FPlease, I urge all of you to calm yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_1323D
        (
            "#13200183V#1601F#5P#NHah! As if I could!\x02\x03",
            "#13200184V#1604FThese bracers are pretty damn good!\x02\x03",
            "#13200185V#1607FI'd heard rumors, but who woulda thought\x01",
            "they'd get me this fired up?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_132F9
        (
            "#13200186V#0006F#6PThat's precisely why I'm telling you\x01",
            "to calm down, Wald...\x02\x03",
            "#13200187V#0001FFirst off, you're in a public space.\x02\x03",
            "#13200188VIf you're dead set on having your matches,\x01",
            "couldn't you at least do everybody a favor\x01",
            "and move them somewhere out of the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_1340B
        (
            "#13200189V#0406F#11PHmmm... No deal.\x02\x03",
            "#13200190V#0402FIsn't it a bit cruel to cut us off right as\x01",
            "things were starting to get exciting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_13498
        "#13200191V#0011F#6PWhat are you saying, Wazy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_134CC
        (
            "#13200192V#0402F#11PWald's totally lost his cool, and those\x01",
            "bracers are just trying to do their job.\x02\x03",
            "#13200193V#0409FShouldn't they stick to their guns and\x01",
            "fight each other?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x36, 500)
    Sleep(300)

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_1358A
        "#13200194V#1602F#6PHaha! Damn straight!\x02",
    )

    CloseMessageWindow()

    def lambda_135BC():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_135BC)
    Sleep(50)

    def lambda_135CC():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_135CC)
    Sleep(300)

    ChrTalk(
        0x36,
        # TAG:CHRTALK_135D7
        (
            "#13200195V#0803F#12PNow that I think about it, I'm actually\x01",
            "kinda peeved, too.\x02\x03",
            "#13200196V#0801FIf we both feel the same way, then maybe\x01",
            "we should settle it. Right here, right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_13691
        "#13200197V#1607F#6PBring it on, girlie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_136BE
        (
            "#13200198V#0006F#6PEnough already!\x02\x03",
            "#13200199V#0013FJoshua! Don't just stand there, say something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        # TAG:CHRTALK_13726
        (
            "#13200200V#0908F#12PSorry, Lloyd. I don't think I can let this\x01",
            "one slide, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1377D
        "#13200201V#0011F#6PWha...\x02",
    )

    CloseMessageWindow()

    def lambda_137A1():

        label("loc_137A1")

        TurnDirection(0xFE, 0x37, 400)
        Yield()
        Jump("loc_137A1")

    QueueWorkItem2(0x38, 0, lambda_137A1)
    Sleep(300)

    ChrTalk(
        0x38,
        # TAG:CHRTALK_137B1
        (
            "#13200202V#0404F#6PI guess I'll be your backup, then, Wald.\x02\x03",
            "#13200203V#0402FYou're strong, sure, but I'm willing to bet\x01",
            "even you would run into trouble going up\x01",
            "against those two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_1386B
        "#13200204V#1603F#5P#NWhatever. Suit yourself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1389E
        "#13200205V#0007F#6PWhy is everybody in this city so damn stubborn?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_138E7
        "#13200206V#0106F#5P(Th-This is spiraling out of control very quickly.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_13933
        (
            "#13200207V#0211F#5P(There is no doubt their dispute will cause a\x01",
            "large disturbance for the citizens.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_1399E
        (
            "#13200208V#0303F#6P#NY'know...\x02\x03",
            "#13200209V#0300FIf you're itchin' for a fight that badly,\x01",
            "then why not settle it some other way?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x38, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4180, 1700, 17780, 1500)

    def lambda_13AC4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13AC4)
    Sleep(50)

    def lambda_13AD4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_13AD4)

    def lambda_13AE1():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_13AE1)
    Sleep(50)

    def lambda_13AF1():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13AF1)

    def lambda_13AFE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13AFE)
    Sleep(50)

    def lambda_13B0E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x38, 0, lambda_13B0E)

    def lambda_13B1B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_13B1B)
    Sleep(50)

    def lambda_13B2B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_13B2B)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_13B35
        "#13200210V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        # TAG:CHRTALK_13B52
        "#13200211V#0405F#5P#NHow so?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_13B75
        (
            "#13200212V#0306F#6PIf they're not able to get all their aggressions\x01",
            "out, it'll sour the rest of the festival for 'em.\x02\x03",
            "#13200213V#0302FBut how about we do it in a way that doesn't\x01",
            "end with everyone all bruised and battered?\x01",
            "A more friendly competition, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        # TAG:CHRTALK_13C7F
        "#13200214V#1601F#5P#NFriendly? What are you talkin' about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        # TAG:CHRTALK_13CBF
        "#13200215V#0805F#11P#NUmm... I'm not sure I follow you, Randy.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_13D04
        "#13200216V#0304F#6PListen up, and be amazed...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(29500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_72_106CD end

    def Function_73_13D68(): pass

    label("Function_73_13D68")

    Sleep(350)
    SetChrChip(0x0, 0x36, 0x1E, 0x12C)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x3)

    def lambda_13D80():
        OP_9D(0xFE, 0x189C, 0x7D0, 0x5078, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_13D80)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x36, 0)
    PlayEffect(0x1, 0xFF, 0x36, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)
    Sleep(150)
    SetChrChip(0x1, 0x36, 0x0, 0x0)
    Return()

    # Function_73_13D68 end

    def Function_74_13DEF(): pass

    label("Function_74_13DEF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -11990, -3000, -9930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2340, -3000, -8610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 19600, -3000, -4370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(885)
    LoadChrToIndex("chr/ch20000.itc", 0x28)
    LoadChrToIndex("chr/ch20100.itc", 0x29)
    LoadChrToIndex("chr/ch20200.itc", 0x2A)
    LoadChrToIndex("chr/ch20300.itc", 0x2B)
    LoadChrToIndex("chr/ch20800.itc", 0x2C)
    LoadChrToIndex("chr/ch20900.itc", 0x2D)
    LoadChrToIndex("chr/ch21200.itc", 0x2E)
    LoadChrToIndex("chr/ch21300.itc", 0x2F)
    LoadChrToIndex("chr/ch21800.itc", 0x30)
    LoadChrToIndex("chr/ch21900.itc", 0x31)
    SetChrChipByIndex(0x44, 0x28)
    SetChrChipByIndex(0x45, 0x29)
    SetChrChipByIndex(0x46, 0x2A)
    SetChrChipByIndex(0x47, 0x2B)
    SetChrChipByIndex(0x48, 0x2C)
    SetChrChipByIndex(0x49, 0x2D)
    SetChrChipByIndex(0x4A, 0x2E)
    SetChrChipByIndex(0x4B, 0x2F)
    SetChrChipByIndex(0x4C, 0x30)
    SetChrChipByIndex(0x4D, 0x31)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x44, 43420, -2500, 1510, 181)
    SetChrPos(0x45, 43370, -2500, -2450, 1)
    SetChrPos(0x46, 42230, -2500, 320, 91)
    SetChrPos(0x47, 41700, -2500, -920, 91)
    SetChrPos(0x48, 39850, -2500, 200, 91)
    SetChrPos(0x49, 39820, -2500, -930, 1)
    SetChrPos(0x4A, 37910, -2500, 70, 91)
    SetChrPos(0x4B, 35970, -2500, -690, 91)
    SetChrPos(0x4C, 34150, -2500, 300, 91)
    SetChrPos(0x4D, 32689, -2500, -390, 91)
    SetChrPos(0x0, 14720, -1000, -920, 135)
    SetChrPos(0x1, 14720, -1000, -920, 135)
    SetChrPos(0x2, 14720, -1000, -920, 135)
    SetChrPos(0x3, 14720, -1000, -920, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x1)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    SetMapObjFrame(0x9, "wave00", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_68(8160, 2600, -2060, 0)
    MoveCamera(21, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(39180, 3000, -8560, 10000)
    MoveCamera(71, 11, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(26500, 10000)
    Sound(885, 2, 90, 0)
    FadeToBright(1000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c047C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_13DEF end

    def Function_75_14188(): pass

    label("Function_75_14188")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 315)
    SetChrPos(0x15, -16920, 0, -9360, 135)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1424F
        (
            "#12P#0000FExcuse us, but we're with the\x01",
            "Crossbell Police Department.\x02\x03",
            "Would this be the Business Owners'\x01",
            "Association's tent? We're here to\x01",
            "follow up on a support request.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x1A, 0xC6, 0x1F4)
    OP_93(0x15, 0xC6, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14337
        "#11POh, you've arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14354
        (
            "#11PNow this is a surprise...I wasn't expecting\x01",
            "you to be the one to come to our aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_143AF
        (
            "#12P#0000FA good surprise, I hope. Your request just\x01",
            "happened to find its way to us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_END)), "loc_14636")

    ChrTalk(
        0x102,
        # TAG:CHRTALK_14412
        "#12P#0100FIt's nice to see you again, Chairman Mors.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x1A, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        # TAG:CHRTALK_14456
        "#5PAre these your friends, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x15, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14485
        (
            "#11PWell... Once upon a time, this young man\x01",
            "sat across from me on a train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_144D6
        (
            "#12P#0000FYeah, that was actually the day I started\x01",
            "working on the force.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1452A():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1452A)

    def lambda_14537():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_14537)
    Sleep(300)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14542
        (
            "#11PAh, yes. It was, wasn't it? At any rate,\x01",
            "I've interacted with these fine folks\x01",
            "a few times since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_145AD
        (
            "#11PWe have a bit of a difficult situation on\x01",
            "our hands. Forgive me for adding more\x01",
            "to your plate, SSS, but we need your help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1485C")

    label("loc_14636")

    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_14640
        "#6P#0205FAre you two already acquainted?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_14678
        (
            "#12P#0000FYeah, we happened to sit across from\x01",
            "each other on the train to Crossbell the\x01",
            "day I started working with you guys.\x02\x03",
            "I had no idea that he was the chairman of the\x01",
            "Business Owners' Association at the time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14758():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14758)

    def lambda_14765():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14765)
    Sleep(300)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14770
        (
            "#11PJust as I was unaware that the young man\x01",
            "across from me was poised to become a\x01",
            "fine detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_147D8
        (
            "#11PWe have a bit of a difficult situation on\x01",
            "our hands. Forgive me for adding more\x01",
            "to your plate, SSS, but we need your help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1485C")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_1485C
        (
            "#12P#0004FYou can count on us, sir.\x02\x03",
            "#0001FLet's see... I believe the request mentioned\x01",
            "something about a recent theft?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_148D9
        "#12P#0301FYeah, wasn't there a bunch of 'em?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_1490B
        "#5PY-Yes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_1492B
        (
            "#5PThere have been four different reports of\x01",
            "theft since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_14974
        "#5PEvery last one of the stalls was robbed clean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_149AB
        (
            "#11PThe Business Owners' Association manages all\x01",
            "of the stalls being run during the festival,\x01",
            "so we hear every report that comes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14A35
        (
            "#11PAfter poring over them all, I've determined\x01",
            "that only food stalls are being targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14A94
        (
            "#11PWe don't have any clues to go off of, so the best\x01",
            "thing we can do is to warn the other stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_14AFC
        (
            "#12P#0101FThat's unfortunate. The vendors already have\x01",
            "enough to worry about during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_14B63
        (
            "#6P#0203FI imagine you are worried about this\x01",
            "damage becoming more widespread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14BB7
        "#11PYes, and that's why I've called you all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14BEE
        (
            "#11PIt is my duty to ensure that the thief is caught before\x01",
            "they can cause any more damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14C4F
        (
            "#11PNot to mention, all this turmoil will no doubt\x01",
            "affect the customers who have come to\x01",
            "enjoy the festival if it continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14CD1
        "#11PWill you please apprehend the thief for us?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_14D1A
        (
            "Accept\x01",      # 0
            "Refuse\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D5F")
    OP_29(0x20, 0x1, 0x1)
    Call(0, 76)
    Return()

    label("loc_14D5F")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_14D5F
        (
            "#12P#0006FSorry, but I don't think we have the time\x01",
            "right now. Our schedule is pretty packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14DC2
        "#11PIs that so? A shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14DE0
        (
            "#11PWell, please come by again if you're up for\x01",
            "the task. I'd like to resolve this before the\x01",
            "thief has a chance to strike again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_14188 end

    def Function_76_14ECA(): pass

    label("Function_76_14ECA")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_14ECA
        (
            "#12P#0001FUnderstood. This is a serious predicament.\x01",
            "We'll begin investigating immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_14F2B
        (
            "#5PThank goodness...\x01",
            "I already feel a little relieved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_14F67
        "#11PI'm counting on all of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_14F8C
        (
            "#12P#0304FRest assured, my man. You're in good hands.\x02\x03",
            "#0301FSo, Lloyd. Any plans on how to tackle this?\x01",
            "We don't have much to go off of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_15020
        (
            "#12P#0003FHmm... You're right. We don't know nearly\x01",
            "enough to try to analyze the situation yet.\x02\x03",
            "#0001FExcuse me. Do you mind telling us which stalls\x01",
            "were targeted? I'd like to speak with the owners.\x02\x03",
            "We may be able to get more information\x01",
            "from them before we proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_15132
        (
            "#11PAh, I see. That makes sense to me.\x01",
            "I've recorded the names down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_15181
        "#11PMay I read them to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_151A2
        "#12P#0100FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_151BE
        (
            "#11PFirst is Nardol's Burgers in Central Square,\x01",
            "followed by Chroma's Juice Stand in\x01",
            "the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_15235
        (
            "#11PNext, we have Palate Pizza in the Entertainment\x01",
            "District and Mithra's Gelato in the Harbor District.\x01",
            "Were you able to get all of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_152C5
        (
            "#12P#0103F*scritch* *scratch* Okay, so four stalls in\x01",
            "total, and they're all in different districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_1532F
        (
            "#6P#0200FNo clues were left, despite there\x01",
            "being four victims?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_15373
        (
            "#12P#0001FWell, let's see what we can dig up from\x01",
            "the owners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_153B6
        (
            "#12P#0000FWill you be here on standby?\x01",
            "We'll return after we've made our rounds.\x02\x03",
            "#0005FOh, yeah. Let me give you my contact information.\x01",
            "Don't hesitate to call us if there are any new\x01",
            "developments.\x02\x03",
            "#0001FWe don't know when the thief will strike again,\x01",
            "so communication is key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_154D2
        "#11PUnderstood. We'll wait here for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_15500
        "#5PWe're counting on you, everyone!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_15545
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_15547
        (
            "Quest \x07\x02",
            "[Serial Theft Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_65(0x4, 0x1)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_76_14ECA end

    def Function_77_15623(): pass

    label("Function_77_15623")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 194)
    SetChrPos(0x15, -16920, 0, -9360, 194)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_156EA
        (
            "#11POh, you're back already.\x01",
            "Were you able to find anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1572C
        (
            "#12P#0000FYeah, we actually managed to\x01",
            "gather a lot of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_15775
        "#12P#0100FWhy don't we sort through it now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_157A6
        "#6P#0200FGood idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_157BF
        "#12P#0300FTake it away, Lloyd.\x02",
    )

    CloseMessageWindow()

    def lambda_157E8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_157E8)

    def lambda_157F5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_157F5)

    def lambda_15802():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15802)

    def lambda_1580F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1580F)
    Sleep(300)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1581A
        "#11P#0001FAll right. Let's try to piece it together.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(-18800, 2400, -13110, 0)
    MoveCamera(39, 34, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21870, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    SetChrPos(0x101, -15680, 0, -12000, 280)
    SetChrPos(0x102, -19550, 0, -12530, 100)
    SetChrPos(0x103, -19450, 0, -11230, 100)
    SetChrPos(0x104, -18070, 0, -13540, 55)
    SetChrPos(0x1A, -16760, 0, -10660, 145)
    SetChrPos(0x15, -18000, 0, -10000, 145)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1590A
        (
            "#11P#0003FAhem... Let's start by going over\x01",
            "everything we've learned thus far.\x02\x03",
            "#0001FBased on what we heard from the stalls' owners,\x01",
            "the thief was able to steal from them by...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_159DF
        (
            "Brandishing a deadly weapon\x01",              # 0
            "Pretending to be a customer\x01",              # 1
            "Striking while they were distracted\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BC5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        # TAG:CHRTALK_15A6C
        (
            "#12P#0301FPretty sure they all said they were hit while they\x01",
            "were in the middle of dealin' with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_15ADC
        (
            "#6P#0203FCommitting the crime while the owners were\x01",
            "busy serving customers to avoid detection...\x02\x03",
            "#0200FA crafty method, I must say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_15B66
        (
            "#11P#0001FYeah, it doesn't matter how cautious you\x01",
            "are if you're too busy to notice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D3D")

    label("loc_15BC5")


    ChrTalk(
        0x104,
        # TAG:CHRTALK_15BC5
        "#12P#0305FWere you payin' attention, pal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_15BF4
        (
            "#6P#0200FThe owners claimed that they were\x01",
            "preoccupied serving customers when\x01",
            "the thief struck.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_15C6E
        (
            "#11P#0005FOh, you're right. They did say that.\x02\x03",
            "#0003FSo, the thief was able to slip in unnoticed\x01",
            "while the owners were busy.\x02\x03",
            "#0001FIt doesn't matter how cautious you are\x01",
            "if you're too busy to notice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D3D")


    ChrTalk(
        0x1A,
        # TAG:CHRTALK_15D3D
        (
            "#5PRight, I had heard the same.\x01",
            "Does their cowardice know no bounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_15D87
        (
            "#12P#0303FLet's not forget our thievin' friend managed\x01",
            "to hit up four of them in a row.\x02\x03",
            "#0301FI bet they're off gloatin' to all their buddies\x01",
            "about their big heist right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_15E42
        (
            "#11P#0001FPerhaps... But, don't crimes like these normally\x01",
            "follow a pattern?\x02\x03",
            "Judging from what I've heard, I think I might\x01",
            "just have an idea of what it is.\x02\x03",
            "#0003FNow that we've pieced together all the information,\x01",
            "it's clear that the criminal's motive was...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_15F60
        (
            "Harassment\x01",               # 0
            "Financial problems\x01",       # 1
            "For their enjoyment\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        # TAG:CHRTALK_15FC3
        (
            "#6P#0101FI get the feeling that the thief was doing\x01",
            "it for their own enjoyment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_16018
        (
            "#6P#0200FCommitting a series of crimes in rapid\x01",
            "succession leads me to believe that they\x01",
            "were not motivated by a lack of mira.\x02\x03",
            "Rather, I believe they were seeking thrills\x01",
            "and getting enjoyment out of stealing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164FF")

    label("loc_160F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16342")

    ChrTalk(
        0x102,
        # TAG:CHRTALK_16104
        (
            "#6P#0105FDo you think they were harassing the stall owners?\x01",
            "The criminals could have been seeking enjoyment\x01",
            "from tormenting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_1618B
        (
            "#6P#0200FI do not think so. The logical course of action\x01",
            "would be to repeatedly target one stall if they\x01",
            "were attempting to harass someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1621C
        (
            "#11P#0006FY-You're right. They never targeted the same\x01",
            "stall twice, so I doubt that was their intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_1628A
        (
            "#12P#0303FGiven that they hit up a bunch of 'em in a row,\x01",
            "I don't think they were in it for the money.\x02\x03",
            "#0301FThey were probably screwin' around and\x01",
            "tryin' to have some fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164FF")

    label("loc_16342")


    ChrTalk(
        0x102,
        # TAG:CHRTALK_16342
        (
            "#6P#0105FCould they have been motivated by financial\x01",
            "problems? I'm not getting that impression, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_163AF
        (
            "#12P#0301FI'm with ya. Hittin' up a bunch of stalls in a\x01",
            "short period of time makes me think they\x01",
            "were doin' it to screw with all of the stall owners.\x02\x03",
            "#0303FThere are plenty of bigger fish to fry\x01",
            "if they needed some serious cash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1649B
        (
            "#11P#0005FY-Yeah, you're right.\x02\x03",
            "#0003FOur criminal probably gets their thrills\x01",
            "from stealing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164FF")


    ChrTalk(
        0x15,
        # TAG:CHRTALK_164FF
        (
            "#5PIt's utterly ridiculous that someone would\x01",
            "commit so many thefts for a reason like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_16560
        "#5PWhat kind of criminal is responsible for this tomfoolery?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_165A3
        (
            "#11P#0003FHmm... I think I have an idea of what the\x01",
            "criminal might be like.\x02\x03",
            "#0001FThe criminal is...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_16622
        (
            "A professional pickpocketer\x01",      # 0
            "A youthful duo\x01",                   # 1
            "A group of bandits\x01",               # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_166A5")
    OP_2C(0x20, 0x2)

    label("loc_166A5")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_166A5
        "#11P#0001FI'm fairly certain it's a pair of younger thieves.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_16744
        "#12P#0305FHow do ya figure? There weren't any witnesses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_16782
        (
            "#11P#0000FThink about it for a second. Each stall was\x01",
            "robbed in the middle of serving a customer.\x02\x03",
            "Didn't the descriptions of the customer they\x01",
            "served sound eerily similar to one another?\x02\x03",
            "#0003FFrom the stalls in the Administrative and\x01",
            "Harbor Districts both described him as\x01",
            "a carefree sort of flirt.\x02\x03",
            "Meanwhile, the stalls in Central Square and\x01",
            "the Entertainment District described him as\x01",
            "a very chatty, energetic kind of guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_16934
        (
            "#6P#0203FThose were the only profiles recounted by the\x01",
            "stall owners at the moment of the theft.\x02\x03",
            "#0200FIt is far too unlikely to be a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_169CC
        (
            "#11P#0001FYeah, that's why I'm thinking our criminals\x01",
            "are a pair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_16A13
        (
            "#6P#0105FI think I get what you're saying...\x02\x03",
            "While one of them garnered the attention of the\x01",
            "stall owner, the other went and stole the mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_16AA6
        (
            "#12P#0303FYeah, makes sense if you assume that they\x01",
            "were switching off their roles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17092")

    label("loc_16B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B9E")

    ChrTalk(
        0x101,
        # TAG:CHRTALK_16B13
        (
            "#11P#0001FI believe it was the work of a\x01",
            "professional pickpocketer.\x02\x03",
            "Their technique was too adept to be\x01",
            "executed by an amateur.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C1C")

    label("loc_16B9E")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_16B9E
        (
            "#11P#0001FI think it may have been a larger\x01",
            "group of thieves.\x02\x03",
            "Their technique was too adept to be\x01",
            "executed by amateurs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C1C")


    ChrTalk(
        0x102,
        # TAG:CHRTALK_16C1C
        (
            "#6P#0103FOr so you'd think...\x02\x03",
            "#0100FBut remember, the stall owners were busy at the\x01",
            "time of the theft. You don't necessarily have to be\x01",
            "skilled at stealing if there's no threat of being caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_16CE4
        "#11P#0005FTh-That's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_16D03
        (
            "#6P#0203FI am concerned, though.\x02\x03",
            "#0200FEach stall was targeted while they were\x01",
            "preoccupied with customers, correct?\x02\x03",
            "Did the descriptions of the customer they\x01",
            "were serving sound eerily similar to you?\x02\x03",
            "#0203FThe stalls in the Administrative and Harbor Districts\x01",
            "both described him as a carefree, flirtatious man.\x02\x03",
            "Meanwhile, the stalls in Central Square and the\x01",
            "Entertainment District described him as very\x01",
            "high-energy and talkative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_16EBB
        (
            "#12P#0305FWell, when you put it that way...\x02\x03",
            "#0301FIt sounds like we're dealin' with\x01",
            "the same two guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_16F28
        (
            "#11P#0001FYeah, it's more than a coincidence that the crimes\x01",
            "were committed while the owners were serving\x01",
            "customers that matched the same profile.\x02\x03",
            "#0003FI'd be willing to bet our thieves work as a duo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_16FF8
        (
            "#6P#0105FI think I get what you're saying...\x02\x03",
            "#0101FWhile one of them garnered the attention of the\x01",
            "stall owner, the other went and stole the goods?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17092")


    ChrTalk(
        0x1A,
        # TAG:CHRTALK_17092
        (
            "#5PWe absolutely cannot let this continue any further.\x01",
            "Please, find them before they strike again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_170FA
        "#5PExactly what he said!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_17118
        (
            "#5PBut how are you going to find them?\x01",
            "The city is packed with people right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_1716E
        (
            "#5PIt's hopeless, isn't it? The best we can do is\x01",
            "alert the shopkeepers to stay on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_171CD
        (
            "#11P#0003FI disagree. I think we have enough information on\x01",
            "how they operate to devise a countermeasure\x01",
            "to stop them from stealing again.\x02\x03",
            "#0001FHey, guys. Where do you think our duo\x01",
            "is going to strike next?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x102,
        # TAG:CHRTALK_172DB
        (
            "#6P#0101FI think it's safe to exclude any stalls\x01",
            "that have already been targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_17332
        (
            "#12P#0300FSooner or later, they're going to get caught\x01",
            "with their hands in the cookie jar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_17392
        (
            "#6P#0200FThat narrows it down to the stalls that have\x01",
            "yet to be burglarized... The question is which.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174F5")
    OP_2C(0x20, 0x1)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1743F
        (
            "#11P#0003F(It's a good thing we interviewed some of\x01",
            "the shopkeepers that were unscathed, too.)\x02\x03",
            "#0001F(I'm pretty certain the one that is most likely\x01",
            "to be targeted is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175AB")

    label("loc_174F5")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_174F5
        (
            "#11P#0003F(Maybe we should have investigated more\x01",
            "of the unaffected stalls, too...)\x02\x03",
            "#0001F(Oh, well. Judging from what we saw, the next\x01",
            "stall most likely to be targeted is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        # TAG:MENU_175BF
        (
            "Central Square's sweets stall\x01",                    # 0
            "Administrative District's omelet rice stall\x01",      # 1
            "Entertainment District's ice cream stall\x01",         # 2
            "Harbor District's noodle stall\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1768B"),
        (1, "loc_17C41"),
        (2, "loc_17EEC"),
        (3, "loc_181B2"),
        (SWITCH_DEFAULT, "loc_183F4"),
    )


    label("loc_1768B")

    OP_2C(0x20, 0x2)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_17690
        "#5PWhat about the sweets stall in Central Square?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_176C7
        (
            "#11P#0001FYeah, that's the one I find most likely, too.\x02\x03",
            "#0003FThe Administrative District will be filled with\x01",
            "officers because of today's parade.\x02\x03",
            "The Entertainment and Harbor Districts\x01",
            "are relatively open areas compared to\x01",
            "Central Square.\x02\x03",
            "#0001FConsidering they need to secure an easily\x01",
            "accessible escape route, Central Square\x01",
            "is the most logical location.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(15)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(12)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_178BF
        "#12P#0305FWhy would they need an escape route?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_178F3
        (
            "#11P#0001FThe shopkeepers that were already stolen from\x01",
            "are going to be more aware of their surroundings.\x02\x03",
            "#0003FEven if we've got an experienced thieves\x01",
            "on our hands, they're far more likely to\x01",
            "get caught at this point.\x02\x03",
            "#0000FAnd they'll need to make a quick getaway\x01",
            "if they do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_17A11
        (
            "#6P#0105FYou know, now that you mention it...\x02\x03",
            "#0100FThe burger stall was also located at the\x01",
            "intersection between a few of the districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_17AA1
        (
            "#6P#0200FThe sweets stall in Central Square is\x01",
            "within proximity of the Back Alley and\x01",
            "the Administrative District.\x02\x03",
            "That area decidedly has the highest number\x01",
            "of escape routes available, so the thieves\x01",
            "are likely to target that stall next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_17B96
        (
            "#12P#0303FGood thinkin', Tio Tot!\x02\x03",
            "#0300FSince it's come down to this, let's stake\x01",
            "it all on the thieves targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0xE)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 4)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_183F4")

    label("loc_17C41")


    ChrTalk(
        0x1A,
        # TAG:CHRTALK_17C41
        (
            "#5PWhat about the omelet stall over in\x01",
            "the Administrative District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_17C8A
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "With the parade happening today,\x01",
            "that area will be unusually congested.\x02\x03",
            "#0001FThe thieves may be able to use the\x01",
            "crowd as a cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_17D39
        (
            "#6P#0101FWon't there be additional police officers for\x01",
            "security purposes, though?\x02\x03",
            "#0103FTrying to commit a crime while surrounded\x01",
            "by law enforcement would pose far too great\x01",
            "a risk, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_17DFE
        "#11P#0006FWh-Whoops. I hadn't considered that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_17E32
        (
            "#12P#0303FWell, better to keep an eye on one stall\x01",
            "than run around in circles.\x02\x03",
            "#0300FLet's stake it all on the thieves targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x11)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 1)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_183F4")

    label("loc_17EEC")


    ChrTalk(
        0x1A,
        # TAG:CHRTALK_17EEC
        (
            "#5PWhat about the ice cream stall over in the\x01",
            "Entertainment District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_17F37
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "I recall the stall being located right\x01",
            "in front of Arc en Ciel.\x02\x03",
            "#0001FThey could make an easy getaway\x01",
            "by slipping through the crowds at the\x01",
            "beginning or end of a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_18012
        (
            "#6P#0205FWould that method not be better suited\x01",
            "for a single thief, though?\x02\x03",
            "#0200FMixing in with the crowd is not quite the same\x01",
            "as actively distracting the stall's owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_180C4
        "#11P#0006FWh-Whoops. I hadn't considered that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_180F8
        (
            "#12P#0303FWell, better to keep an eye on one stall\x01",
            "than run around in circles.\x02\x03",
            "#0300FLet's stake it all on the thieves targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x12)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_183F4")

    label("loc_181B2")


    ChrTalk(
        0x1A,
        # TAG:CHRTALK_181B2
        "#5PWhat about the noodle stall in the Harbor District?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_181EE
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "#0001FThough it's the stall closest to this tent...\x01",
            "they might try to take advantage of us\x01",
            "waving it off as a way-too-obvious target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_1829F
        (
            "#6P#0103FI know we assumed they're thrill seekers,\x01",
            "but that might be too much of a risk even\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1830B
        "#11P#0006FUrgh... Maybe that WAS a bit of a reach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_18343
        (
            "#12P#0303FWell, better to keep an eye on one stall\x01",
            "than run around in circles.\x02\x03",
            "#0300FLet's stake it all on the thieves targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x13)
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 83)
    Jump("loc_183F4")

    label("loc_183F4")

    Return()

    # Function_77_15623 end

    def Function_78_183F5(): pass

    label("Function_78_183F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch23600.itc", 0x29)
    LoadChrToIndex("chr/ch30000.itc", 0x2A)
    LoadChrToIndex("chr/ch02708.itc", 0x2B)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-20590, 2500, -12420, 0)
    MoveCamera(64, 28, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -19640, 0, -10290, 90)
    SetChrPos(0x102, -18810, 0, -12750, 20)
    SetChrPos(0x103, -19720, 0, -11730, 65)
    SetChrPos(0x104, -17130, 0, -12710, 335)
    SetChrPos(0x1A, -15910, 0, -10370, 245)
    SetChrPos(0x15, -16920, 0, -9360, 200)
    SetChrPos(0x4E, -17790, 0, -11400, 20)
    SetChrPos(0x4F, -18560, 0, -10890, 20)
    SetChrPos(0x50, -19300, 0, -3440, 20)
    SetChrPos(0x51, -20380, 0, -3260, 20)
    SetChrPos(0x52, -15180, 0, -11440, 300)
    SetChrChipByIndex(0x4E, 0x28)
    SetChrSubChip(0x4E, 0x0)
    SetChrChipByIndex(0x4F, 0x29)
    SetChrSubChip(0x4F, 0x0)
    SetChrChipByIndex(0x50, 0x2A)
    SetChrSubChip(0x50, 0x0)
    SetChrChipByIndex(0x51, 0x2A)
    SetChrSubChip(0x51, 0x0)
    SetChrChipByIndex(0x52, 0x2B)
    SetChrSubChip(0x52, 0x0)
    ClearChrFlags(0x4E, 0x80)
    ClearChrBattleFlags(0x4E, 0x8000)
    ClearChrFlags(0x4F, 0x80)
    ClearChrBattleFlags(0x4F, 0x8000)
    ClearChrFlags(0x50, 0x80)
    ClearChrBattleFlags(0x50, 0x8000)
    ClearChrFlags(0x51, 0x80)
    ClearChrBattleFlags(0x51, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18572")
    ClearChrFlags(0x52, 0x80)
    ClearChrBattleFlags(0x52, 0x8000)

    label("loc_18572")

    BeginChrThread(0x4E, 0, 0, 79)
    BeginChrThread(0x4F, 0, 0, 79)
    OP_52(0x4E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x4E,
        # TAG:CHRTALK_185C6
        (
            "#11PYou're all just a bunch of spineless cops!\x01",
            "The hell do you think you can do to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        # TAG:CHRTALK_18622
        (
            "#5PYa think you can just walk all over us,\x01",
            "the Black Emperors?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186FC")

    ChrTalk(
        0x52,
        # TAG:CHRTALK_18675
        "#11P#1207FGrrrrrrrrowl!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)

    def lambda_1869F():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_1869F)

    def lambda_186AC():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_186AC)
    Sleep(200)
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x4E,
        # TAG:CHRTALK_186DE
        "#11PEeek! W-We're sorry!\x02",
    )

    CloseMessageWindow()

    label("loc_186FC")


    ChrTalk(
        0x15,
        # TAG:CHRTALK_186FC
        (
            "#5PI'm relieved that we were able to retrieve the mira...\x01",
            "But I must say, these hooligans aren't quite as\x01",
            "rough around the edges as I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_18796
        (
            "#12P#0306FYou said it, pal.\x02\x03",
            "#0300FOne punch from the downtown delinquents,\x01",
            "and they'd be cryin' like a bunch of pansies.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)
    OP_63(0x4E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x4F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_18856():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18856)

    def lambda_18873():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18873)
    Sleep(1200)
    OP_63(0x4E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x4F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_188B5
        "#6P#0005FWow, that quieted them down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_188E0
        (
            "#12P#0105FDo you think it's possible they really\x01",
            "were threatened by them?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18934():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18934)

    def lambda_18941():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18941)
    Sleep(200)

    ChrTalk(
        0x4E,
        # TAG:CHRTALK_1894C
        (
            "#11PWh-Wh-Who'd ever get scared by guys\x01",
            "like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        # TAG:CHRTALK_18985
        (
            "#5PYou makin' fun of us or somethin'?!\x01",
            "We'd have no trouble takin' 'em on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_189D5
        (
            "#6P#0200FWe have our answer.\x02\x03",
            "I see now. They were made fools of,\x01",
            "so they resorted to petty crimes as a\x01",
            "means of venting their frustration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_18A66
        "#11PSo that's what it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_18A86
        (
            "#11PThey've disrupted the festival, and for what?\x01",
            "Some selfish, self-pitying reason?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18AE5():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18AE5)

    def lambda_18AF2():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18AF2)
    Sleep(300)
    SetCameraDistance(19210, 1600)
    OP_95(0x1A, -16880, 0, -10300, 1000, 0x0)

    def lambda_18B1F():
        OP_93(0xFE, 0xF5, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18B1F)
    OP_93(0x1A, 0xF5, 0x190)
    Sleep(300)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_18B31
        (
            "#11PYou hooligans made a big mistake. You'd better\x01",
            "be ready to answer for your crimes in full.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    ChrTalk(
        0x4E,
        # TAG:CHRTALK_18BBC
        (
            "#12PUgh...\x01",
            "(What's with this old geezer?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        # TAG:CHRTALK_18BEB
        (
            "#6P*gulp*\x01",
            "(That glare is giving me chills...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x50,
        # TAG:NPCTALK_18C1E
        "Voice",
        (
            "#4POh, there you are. You're the\x01",
            "Special Support Section, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-19920, 2500, -11390, 2500)
    MoveCamera(53, 31, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(20320, 2500)

    def lambda_18C9E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_18C9E)

    def lambda_18CAB():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_18CAB)

    def lambda_18CB8():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_18CB8)

    def lambda_18CC5():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_18CC5)

    def lambda_18CD2():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_18CD2)

    def lambda_18CDF():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18CDF)

    def lambda_18CEC():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18CEC)

    def lambda_18CF9():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18CF9)

    def lambda_18D06():
        OP_95(0xFE, -19300, 0, -7440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_18D06)

    def lambda_18D20():
        OP_95(0xFE, -20380, 0, -7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_18D20)
    Sleep(2500)

    ChrTalk(
        0x50,
        # TAG:CHRTALK_18D38
        "#11PSorry we're late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x51,
        # TAG:CHRTALK_18D53
        "#5PWe're here to take away the thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_18D80
        (
            "#12P#0001FThanks. Sorry for calling you out here\x01",
            "during such a busy period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x50,
        # TAG:CHRTALK_18DD1
        "#11PNot a problem. It's our job, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x50,
        # TAG:CHRTALK_18E02
        "#11PAre these two the guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_18E23
        "#12P#0001FYeah. If you would escort them to HQ, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x51,
        # TAG:CHRTALK_18E60
        "#5PRight. You can count on us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x4E, -19770, 0, -6410, 341)
    SetChrPos(0x4F, -20770, 0, -6710, 0)
    SetChrPos(0x1A, -18220, 0, -9760, 315)
    SetChrPos(0x15, -18050, 0, -8480, 315)
    SetChrPos(0x50, -19220, 0, -7200, 341)
    SetChrPos(0x51, -21370, 0, -7320, 26)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x50,
        # TAG:CHRTALK_18EFF
        "#11PHey, move it along!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x4E,
        # TAG:CHRTALK_18F1C
        "#11PWhoa! Don't push me!\x02",
    )

    CloseMessageWindow()

    def lambda_18F3F():

        label("loc_18F3F")

        TurnDirection(0xFE, 0x51, 400)
        Yield()
        Jump("loc_18F3F")

    QueueWorkItem2(0x1A, 1, lambda_18F3F)

    def lambda_18F51():

        label("loc_18F51")

        TurnDirection(0xFE, 0x50, 400)
        Yield()
        Jump("loc_18F51")

    QueueWorkItem2(0x15, 1, lambda_18F51)

    def lambda_18F63():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18F63)

    def lambda_18F70():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18F70)

    def lambda_18F7D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_18F7D)

    def lambda_18F8A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_18F8A)
    Sleep(100)

    def lambda_18F9A():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18F9A)

    def lambda_18FAF():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18FAF)

    def lambda_18FC4():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_18FC4)

    def lambda_18FD9():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_18FD9)
    Sleep(6000)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x15, 0x1)
    OP_68(-20430, 2500, -11880, 2000)
    MoveCamera(69, 29, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(20320, 2000)

    def lambda_19027():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19027)

    def lambda_19034():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19034)

    def lambda_19041():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19041)

    def lambda_1904E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1904E)
    BeginChrThread(0x1A, 1, 0, 80)
    Sleep(100)
    BeginChrThread(0x15, 1, 0, 81)
    Sleep(300)
    SetChrFlags(0x4E, 0x80)
    SetChrBattleFlags(0x4E, 0x8000)
    SetChrFlags(0x4F, 0x80)
    SetChrBattleFlags(0x4F, 0x8000)
    SetChrFlags(0x50, 0x80)
    SetChrBattleFlags(0x50, 0x8000)
    SetChrFlags(0x51, 0x80)
    SetChrBattleFlags(0x51, 0x8000)

    ChrTalk(
        0x15,
        # TAG:CHRTALK_19090
        "#5PPhew... Looks like it's case closed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_190BD
        (
            "#12P#0100FThey didn't look like they were from Crossbell,\x01",
            "so I figure they won't be in jail for more than\x01",
            "three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_19138
        "#12P#0306FCrossbell's pretty soft on the foreigners, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19176
        (
            "#11PHaha. Yes, well, the joke is on them. They'll be\x01",
            "sitting in a jail cell staring at a stone wall, while\x01",
            "the rest of us are out here enjoying the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19219
        (
            "#11PNot to mention...I had a bit of fun striking\x01",
            "fear into their hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_19267
        (
            "#6P#0205FI must say, your charade was spectacular.\x01",
            "They were completely fooled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_192BC
        (
            "#11PHaha. It comes with the experience of being a\x01",
            "veteran trader. I'm used to having to put on airs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_19326
        "#6P#0000FIt's definitely a side of you I've never seen before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_195E7")

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19377
        (
            "#11PI think I put on quite the performance,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_193BF
        "#11PThank you for resolving the issue, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_193F5
        "#5PIndeed. We're truly in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        # TAG:CHRTALK_1941F
        (
            "#5PPlease allow for the Business Owners' Association\x01",
            "to present you its utmost gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1947E
        (
            "#6P#0000FOh, no. That won't be necessary. We're just\x01",
            "glad to have solved the case before any\x01",
            "more damage was dealt.\x02\x03",
            "You know where to find us if you ever run into\x01",
            "any other problems. We'd be happy to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19552
        (
            "#11PA fine plan, indeed. It's comforting to know\x01",
            "I'm in good hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_1959B
        "#12P#0100FDon't be afraid to reach out to us anytime.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    Jump("loc_19A7C")

    label("loc_195E7")


    ChrTalk(
        0x101,
        # TAG:CHRTALK_195E7
        (
            "#6P#0006FI'm sorry, everyone. Looks like my\x01",
            "deduction was a little off the mark.\x02\x03",
            "They almost managed to slip away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_19660
        (
            "#12P#0106FWe feel terribly sorry, and after you put\x01",
            "your faith in us, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_196B2
        (
            "#11PNo, no. That's quite all right. You were\x01",
            "able to resolve it, and that's what matters.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x87, 0x190)

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19718
        (
            "#11PNot to mention, that excellent police dog\x01",
            "of yours... Zeit was his name, I believe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_19775
        (
            "#11PYou considered a worst-case scenario, and\x01",
            "masterfully deployed him. I was impressed\x01",
            "to see that level of reasoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_197F2
        "#6P#0012FHa...hahaha... Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x52,
        # TAG:CHRTALK_19820
        "#11P#1203FGrrrrowl...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x52, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        # TAG:CHRTALK_19845
        "#6P#0203FHe says we still have a long road ahead of us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        # TAG:CHRTALK_198D3
        "#12P#0306FDamn. We really screwed that one up.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0xE1, 0x190)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x15,
        # TAG:CHRTALK_1994F
        (
            "#5PIt's all right. You still tried to help us. On behalf\x01",
            "of the Business Owners' Association, allow us\x01",
            "to thank you for your service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        # TAG:CHRTALK_199DA
        (
            "#11PWe may rely on you again when the time\x01",
            "comes. Please lend us your strength\x01",
            "when it does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_19A3C
        "#12P#0100FWe'd be glad to be of service again.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)

    label("loc_19A7C")

    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_19A98
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_19A9A
        (
            "Quest \x07\x02",
            "[Serial Theft Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    SetChrFlags(0x52, 0x80)
    SetChrBattleFlags(0x52, 0x8000)
    OP_49()
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x20, 0x4, 0x10)
    SetScenarioFlags(0x2, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_183F5 end

    def Function_79_19B8D(): pass

    label("Function_79_19B8D")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_19BCD"),
        (1, "loc_19BD9"),
        (2, "loc_19BE5"),
        (3, "loc_19BF1"),
        (4, "loc_19BFD"),
        (5, "loc_19C09"),
        (6, "loc_19C15"),
        (SWITCH_DEFAULT, "loc_19C21"),
    )


    label("loc_19BCD")

    OP_A0(0xFE, 2450, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19BD9")

    OP_A0(0xFE, 2550, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19BE5")

    OP_A0(0xFE, 2600, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19BF1")

    OP_A0(0xFE, 2400, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19BFD")

    OP_A0(0xFE, 2650, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19C09")

    OP_A0(0xFE, 2350, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19C15")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19C21")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19C2D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19C90")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_19C60"),
        (1, "loc_19C6C"),
        (2, "loc_19C78"),
        (SWITCH_DEFAULT, "loc_19C84"),
    )


    label("loc_19C60")

    OP_93(0xFE, 0x2D, 0x1F4)
    Jump("loc_19C84")

    label("loc_19C6C")

    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("loc_19C84")

    label("loc_19C78")

    OP_93(0xFE, 0x87, 0x1F4)
    Jump("loc_19C84")

    label("loc_19C84")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_19C2D")

    label("loc_19C90")

    Return()

    # Function_79_19B8D end

    def Function_80_19C91(): pass

    label("Function_80_19C91")

    OP_95(0xFE, -16940, 0, -10040, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_80_19C91 end

    def Function_81_19CAD(): pass

    label("Function_81_19CAD")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, -17600, 0, -9230, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_81_19CAD end

    def Function_82_19CD0(): pass

    label("Function_82_19CD0")

    EventBegin(0x0)
    OP_4B(0x10, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12800, 2510, 10130, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrPos(0x101, 14260, 10, 10900, 0)
    SetChrPos(0x102, 15680, 10, 9480, 0)
    SetChrPos(0x103, 15680, 10, 10900, 0)
    SetChrPos(0x104, 14260, 10, 9480, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_19D67
        (
            "#12P#0309F'Mithra's Gelato,' huh? A gorgeous girl\x01",
            "like her's got my heart melting already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_19DC7
        (
            "#6P#0006FSave the flirting for another time, Randy.\x01",
            "We're here for a reason.\x02\x03",
            "#0001FLet's see what we can find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_19E40
        (
            "#0100FExcuse us, ma'am. We're here with the CPD.\x01",
            "May we have a moment to ask you about\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_19EAB
        (
            "#5POf course. You're talking about the\x01",
            "theft, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_19EE5
        (
            "#5PHe managed to pull a fast one on me\x01",
            "while I was serving a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_19F31
        "#12P#0200FHe struck while you were busy, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_19F65
        (
            "#5PYeah, I had my hands full serving this\x01",
            "laid-back tourist guy that was trying his\x01",
            "hardest to hit on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_19FD4
        (
            "#5PWhile I was warding off his persistent\x01",
            "advances, I thought I sensed someone\x01",
            "sneaking around behind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_1A043
        (
            "#5PBut, it was too little, too late. By the time\x01",
            "I turned around, the register had already\x01",
            "been emptied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A0B1
        (
            "#6P#0001FI suppose you wouldn't know anything\x01",
            "about the thief, in that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        # TAG:CHRTALK_1A103
        (
            "#5PI'm afraid not... Ugh! I can't believe\x01",
            "I let them slip right under my nose!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3C2")
    OP_68(13510, 2510, 9070, 1200)
    MoveCamera(45, 24, 0, 1200)

    def lambda_1A1A3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A1A3)

    def lambda_1A1B0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A1B0)

    def lambda_1A1BD():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A1BD)

    def lambda_1A1CA():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A1CA)
    Sleep(1200)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A1D5
        "#6P#0003FI think we've heard everything she has to offer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        # TAG:CHRTALK_1A214
        (
            "#12P#0300FYeah, sounds 'bout right. Wanna head back\x01",
            "and sort through the details?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A3BC")

    ChrTalk(
        0x102,
        # TAG:CHRTALK_1A2A6
        (
            "#0100FWe haven't heard from the Business Owners'\x01",
            "Association, so we can assume that\x01",
            "no other stalls have been victimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        # TAG:CHRTALK_1A325
        (
            "#11P#0203FThat should be the case, yes.\x02\x03",
            "#0200FThough, perhaps it would be prudent\x01",
            "to conduct one more round of the food\x01",
            "stalls, just to be sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3BC")

    OP_29(0x20, 0x1, 0xD)

    label("loc_1A3C2")

    OP_5A()
    SetChrPos(0x0, 14780, 10, 10480, 0)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_82_19CD0 end

    def Function_83_1A3E5(): pass

    label("Function_83_1A3E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(806)
    OP_68(-12140, 2500, 10400, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(31380, 0)
    SetChrPos(0x101, -2510, -700, 2200, 315)
    SetChrPos(0x102, -3310, -700, 3000, 315)
    SetChrPos(0x103, -3710, -700, 1390, 315)
    SetChrPos(0x104, -4520, -700, 2180, 315)
    SetChrPos(0x44, -10280, 0, 11510, 0)
    SetChrPos(0x45, 1440, 0, 10420, 45)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x45, 0x4)
    SetChrChipByIndex(0x44, 0x18)
    SetChrSubChip(0x44, 0x0)
    SetChrChipByIndex(0x45, 0x9)
    SetChrSubChip(0x45, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    SetChrName(
        # TAG:CHRNAME_1A4D0
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_1A4D2
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The SSS made their way over to the noodle stall to\x01",
            "conduct their stakeout.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-12140, 1500, 10400, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x44, 1, 0, 84)
    OP_0D()
    OP_6F(0x1)

    AnonymousTalk(
        0x101,
        # TAG:ANONTALK_1A562
        (
            "#0001F...\x02\x03",
            "I don't see any signs of our thief...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x44, 0x1)
    OP_64(0x9)
    OP_64(0x44)
    Sleep(200)
    OP_95(0x44, 1370, 0, 11710, 1500, 0x0)
    Sleep(1800)
    OP_95(0x45, -10170, 0, 10420, 1500, 0x0)
    OP_95(0x45, -10170, 0, 11550, 1500, 0x0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x45, 1, 0, 84)
    Sleep(2500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x45, 0x1)
    OP_64(0x9)
    OP_64(0x45)
    Sleep(200)
    OP_95(0x45, -14300, 0, 13120, 1500, 0x0)
    OP_95(0x45, -14300, 2000, 23040, 1500, 0x0)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)

    AnonymousTalk(
        0x104,
        # TAG:ANONTALK_1A649
        "#0306FYeah... Not a one.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        # TAG:ANONTALK_1A667
        "#0200FAnd it has already been an hour...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        # TAG:ANONTALK_1A695
        (
            "#0001FI don't get it. If they were coming,\x01",
            "they should have shown up by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-4170, 1840, 1020, 0)
    MoveCamera(3, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13040, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x87, 0x190)
    Sleep(50)

    def lambda_1A745():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A745)

    def lambda_1A752():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A752)

    def lambda_1A75F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A75F)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A79F
        (
            "#11P#0003FHello? Lloyd Bannings spea--\x02\x03",
            "#0005FThe thieves showed up?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A841
        (
            "#11P#0001FC-Central Square? Got it!\x02\x03",
            "We'll be there right away!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A8B0
        (
            "#11P#0006FSorry, guys. It looks like my deductions\x01",
            "were a little off target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        # TAG:CHRTALK_1A902
        "#5P#0101FIt's fine. Let's hurry, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        # TAG:CHRTALK_1A92F
        "#11P#0001FR-Right. Let's go!\x02",
    )

    CloseMessageWindow()

    def lambda_1A956():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A956)

    def lambda_1A963():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A963)

    def lambda_1A970():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A970)

    def lambda_1A97D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A97D)
    Sleep(300)

    def lambda_1A98D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A98D)

    def lambda_1A9A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A9A2)

    def lambda_1A9B7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A9B7)

    def lambda_1A9CC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A9CC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_1A3E5 end

    def Function_84_1A9F9(): pass

    label("Function_84_1A9F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AA1E")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_84_1A9F9")

    label("loc_1AA1E")

    Return()

    # Function_84_1A9F9 end

    def Function_85_1AA1F(): pass

    label("Function_85_1AA1F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    SetChrName(
        # TAG:CHRNAME_1AA2C
        ""
    )

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_1AA37
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "        Lupinus River - Lighthouse 1\x01\x01",
            "Unauthorized entry is strictly prohibited.\x01",
            "                                 - City Hall\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(-1, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_85_1AA1F end

    def Function_86_1AAD5(): pass

    label("Function_86_1AAD5")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)

    SetChrName(
        # TAG:CHRNAME_1AAE0
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_1AAE2
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A sign is affixed to the locked door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    SetChrName(
        # TAG:CHRNAME_1AB27
        ""
    )


    AnonymousTalk(
        0xFF,
        # TAG:ANONTALK_1AB29
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  Heiyue Trading, Ltd. - Crossbell Branch\x01",
            "If you have business with us, please knock.",
            scpstr(0xD),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(-1, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_86_1AAD5 end

    SaveToFile()

Try(main)
