#!/usr/bin/python3

# load all necessary modules
import socket
import crcmod
import time
import sys

# create register command list
cmd_04 = [

# This command description and expected values have been defined in the EDP publication DEF-C44-509/N
#####################################################################################################

# Index  Field name                                                               Type         Unit    Scaler
[   '0', "",                                                                      "",          "",     ""   ],
[   '1', "clock",                                                                 "clock",     "-",    "-"  ],
[   '2', "Device ID 1 - Device Serial Number",                                    "octet",     "-",    "-"  ],
[   '3', "Device ID 2 - Manufacturer Model Codes and Year",                       "octet",     "-",    "-"  ],
[   '4', "Active core firmware Id.",                                              "octet",     "-",    "-"  ],
[   '5', "Active app firmware Id.",                                               "octet",     "-",    "-"  ],
[   '6', "Active com firmware Id.",                                               "octet",     "-",    "-"  ],
[   '7', "HAN interface - Modbus address",                                        "unsigned",  "-",    "-"  ],
[   '8', "HAN interface - Access profile",                                        "bitString", "-",    "-"  ],
[   '9', "Status control",                                                        "octet",     "-",    "-"  ],
[  '10', "Activity Calendar - Active Name",                                       "octet",     "-",    "-"  ],
[  '11', "Currently active tariff",                                               "unsigned",  "-",    "-"  ],
[  '12', "Active demand control threshold T1",                                    "double",    "VA",   "0"  ],
[  '13', "Active demand control threshold T2",                                    "double",    "VA",   "0"  ],
[  '14', "Active demand control threshold T3",                                    "double",    "VA",   "0"  ],
[  '15', "Active demand control threshold T4",                                    "double",    "VA",   "0"  ],
[  '16', "Active demand control threshold T5",                                    "double",    "VA",   "0"  ],
[  '17', "Active demand control threshold T6",                                    "double",    "VA",   "0"  ],
[  '18', "Currently apparent power threshold",                                    "double",    "VA",   "0"  ],
[  '19', "Demand management status",                                              "demand",    "-",    "-"  ],
[  '20', "Demand management period definition",                                   "demand",    "-",    "-"  ],
[  '21', "Residual power threshold",                                              "double",    "VA",   "0"  ],
[  '22', "Active energy import (+A)",                                             "double",    "Wh",   "0"  ],
[  '23', "Active energy export (-A)",                                             "double",    "Wh",   "0"  ],
[  '24', "Reactive energy QI (+Ri)",                                              "double",    "VArh", "0"  ],
[  '25', "Reactive energy QII (+Rc)",                                             "double",    "VArh", "0"  ],
[  '26', "Reactive energy QIII (-Ri)",                                            "double",    "VArh", "0"  ],
[  '27', "Reactive energy QIV (-Rc)",                                             "double",    "VArh", "0"  ],
[  '28', "Active energy import (+A) L1",                                          "double",    "Wh",   "0"  ],
[  '29', "Active energy import (+A) L2",                                          "double",    "Wh",   "0"  ],
[  '30', "Active energy import (+A) L3",                                          "double",    "Wh",   "0"  ],
[  '31', "Active energy export (-A) L1",                                          "double",    "Wh",   "0"  ],
[  '32', "Active energy export (-A) L2",                                          "double",    "Wh",   "0"  ],
[  '33', "Active energy export (-A) L3",                                          "double",    "Wh",   "0"  ],
[  '34', "Max demand active power + (QI+QIV)",                                    "double",    "W",    "0"  ],
[  '35', "Max demand active power + (QI+QIV) (capture time)",                     "clock",     "-",    "-"  ],
[  '36', "Max demand active power - (QII+QIII)",                                  "double",    "W",    "0"  ],
[  '37', "Max demand active power - (QII+QIII) (capture time)",                   "clock",     "-",    "-"  ],
[  '38', "Rate 1 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '39', "Rate 2 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '40', "Rate 3 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '41', "Rate 4 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '41', "Rate 5 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '43', "Rate 6 contract 1 active energy (+A)",                                  "double",    "Wh",   "0"  ],
[  '44', "Total Rate contract 1 active energy (+A)",                              "double",    "Wh",   "0"  ],
[  '45', "Rate 1 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '46', "Rate 2 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '47', "Rate 3 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '48', "Rate 4 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '49', "Rate 5 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '50', "Rate 6 contract 1 active energy (-A)",                                  "double",    "Wh",   "0"  ],
[  '51', "Total Rate contract 1 active energy (-A)",                              "double",    "Wh",   "0"  ],
[  '52', "Rate 1 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '53', "Rate 2 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '54', "Rate 3 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '55', "Rate 4 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '56', "Rate 5 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '57', "Rate 6 contract 1 reactive energy QI (+Ri)",                            "double",    "VArh", "0"  ],
[  '58', "Total Rate contract 1 reactive energy QI (+Ri)",                        "double",    "VArh", "0"  ],
[  '59', "Rate 1 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '60', "Rate 2 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '61', "Rate 3 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '62', "Rate 4 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '63', "Rate 5 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '64', "Rate 6 contract 1 reactive energy QII (+Rc)",                           "double",    "VArh", "0"  ],
[  '65', "Total Rate contract 1 reactive energy QII (+Rc)",                       "double",    "VArh", "0"  ],
[  '66', "Rate 1 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '67', "Rate 2 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '68', "Rate 3 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '69', "Rate 4 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '70', "Rate 5 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '71', "Rate 6 contract 1 reactive energy QIII (-Ri)",                          "double",    "VArh", "0"  ],
[  '72', "Total Rate contract 1 reactive energy QIII (-Ri)",                      "double",    "VArh", "0"  ],
[  '73', "Rate 1 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '74', "Rate 2 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '75', "Rate 3 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '76', "Rate 4 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '77', "Rate 5 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '78', "Rate 6 contract 1 reactive energy QIV (-Rc)",                           "double",    "VArh", "0"  ],
[  '79', "Total Rate contract 1 reactive energy QIV (-Rc)",                       "double",    "VArh", "0"  ],
[  '80', "Rate 1 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '81', "Rate 1 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '82', "Rate 2 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '83', "Rate 2 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '84', "Rate 3 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '85', "Rate 3 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '86', "Rate 4 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '87', "Rate 4 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '88', "Rate 5 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '89', "Rate 5 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '90', "Rate 6 contract 1 Maximum demand active power + (last average)",        "double",    "W",    "0"  ],
[  '91', "Rate 6 contract 1 Maximum demand active power + (capture time)",        "clock",     "-",    "-"  ],
[  '92', "Total Rate contract 1 Maximum demand active power + (last average)",    "double",    "W",    "0"  ],
[  '93', "Total Rate contract 1 Maximum demand active power + (capture time)",    "clock",     "-",    "-"  ],
[  '94', "Rate 1 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[  '95', "Rate 1 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[  '96', "Rate 2 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[  '97', "Rate 2 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[  '98', "Rate 3 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[  '99', "Rate 3 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[ '100', "Rate 4 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[ '101', "Rate 4 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[ '102', "Rate 5 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[ '103', "Rate 5 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[ '104', "Rate 6 contract 1 Maximum demand active power - (last average)",        "double",    "W",    "0"  ],
[ '105', "Rate 6 contract 1 Maximum demand active power - (capture time)",        "clock",     "-",    "-"  ],
[ '106', "Total Rate contract 1 Maximum demand active power - (last average)",    "double",    "W",    "0"  ],
[ '107', "Total Rate contract 1 Maximum demand active power - (capture time)",    "clock",     "-",    "-"  ],
[ '108', "Instantaneous Voltage L1",                                              "long",      "V",    "-1" ],
[ '109', "Instantaneous Current L1",                                              "long",      "A",    "-1" ],
[ '110', "Instantaneous Voltage L2",                                              "long",      "V",    "-1" ],
[ '111', "Instantaneous Current L2",                                              "long",      "A",    "-1" ],
[ '112', "Instantaneous Voltage L3",                                              "long",      "V",    "-1" ],
[ '113', "Instantaneous Current L3",                                              "long",      "A",    "-1" ],
[ '114', "Instantaneous Current (Sum of all phases)",                             "long",      "A",    "-1" ],
[ '115', "Instantaneous Active power + L1",                                       "double",    "W",    "0"  ],
[ '116', "Instantaneous Active power - L1",                                       "double",    "W",    "0"  ],
[ '117', "Instantaneous Active power + L2",                                       "double",    "W",    "0"  ],
[ '118', "Instantaneous Active power - L2",                                       "double",    "W",    "0"  ],
[ '119', "Instantaneous Active power + L3",                                       "double",    "W",    "0"  ],
[ '120', "Instantaneous Active power - L3",                                       "double",    "W",    "0"  ],
[ '121', "Instantaneous Active power + (Sum of all phases)",                      "double",    "W",    "0"  ],
[ '122', "Instantaneous Active power - (Sum of all phases)",                      "double",    "W",    "0"  ],
[ '123', "Instantaneous Power factor",                                            "long",      "-",    "-3" ],
[ '124', "Instantaneous Power factor L1",                                         "long",      "-",    "-3" ],
[ '125', "Instantaneous Power factor L2",                                         "long",      "-",    "-3" ],
[ '126', "Instantaneous Power factor L3",                                         "long",      "-",    "-3" ],
[ '127', "Instantaneous Frequency",                                               "long",      "Hz",   "-1" ],
[ '128', "Load profile - Configured measurements",                                "array",     "-",    "-"  ],
[ '129', "Load profile - Capture period",                                         "double",    "s",    "0"  ],
[ '130', "Load profile - Entries in use",                                         "double",    "-",    "-"  ],
[ '131', "Load profile - Profile entries",                                        "double",    "-",    "-"  ],
[ '132', "disconnect control state",                                              "disconnect","-",    "-"  ],
[ '133', "disconnector Q parameter",                                              "double",    "-",    "-"  ],
[ '134', "disconnector K parameter",                                              "double",    "%",    "0"  ],
[ '135', "Reactive energy QI (+Ri) L1",                                           "double",    "Wh",   "0"  ],
[ '136', "Reactive energy QI (+Ri) L2",                                           "double",    "Wh",   "0"  ],
[ '137', "Reactive energy QI (+Ri) L3",                                           "double",    "Wh",   "0"  ],
[ '138', "Reactive energy QII (+Rc) L1",                                          "double",    "Wh",   "0"  ],
[ '139', "Reactive energy QII (+Rc) L2",                                          "double",    "Wh",   "0"  ],
[ '140', "Reactive energy QII (+Rc) L3",                                          "double",    "Wh",   "0"  ],
[ '141', "Reactive energy QIII (-Ri) L1",                                         "double",    "Wh",   "0"  ],
[ '142', "Reactive energy QIII (-Ri) L2",                                         "double",    "Wh",   "0"  ],
[ '143', "Reactive energy QIII (-Ri) L3",                                         "double",    "Wh",   "0"  ],
[ '144', "Reactive energy QIV (-Rc) L1",                                          "double",    "Wh",   "0"  ],
[ '145', "Reactive energy QIV (-Rc) L2",                                          "double",    "Wh",   "0"  ],
[ '146', "Reactive energy QIV (-Rc) L3",                                          "double",    "Wh",   "0"  ],
[ '147', "Max demand active power + (QI+QIV) L1",                                 "double",    "W",    "0"  ],
[ '148', "Max demand active power + (QI+QIV) L1 (capture time)",                  "clock",     "-",    "-"  ],
[ '149', "Max demand active power + (QI+QIV) L2",                                 "double",    "W",    "0"  ],
[ '150', "Max demand active power + (QI+QIV) L2 (capture time)",                  "clock",     "-",    "-"  ],
[ '151', "Max demand active power + (QI+QIV) L3",                                 "double",    "W",    "0"  ],
[ '152', "Max demand active power + (QI+QIV) L3 (capture time)",                  "clock",     "-",    "-"  ],
[ '153', "Max demand active power - (QII+QIII) L1",                               "double",    "W",    "0"  ],
[ '154', "Max demand active power - (QII+QIII) L1 (capture time)",                "clock",     "-",    "-"  ],
[ '155', "Max demand active power - (QII+QIII) L2",                               "double",    "W",    "0"  ],
[ '156', "Max demand active power - (QII+QIII) L2 (capture time)",                "clock",     "-",    "-"  ],
[ '157', "Max demand active power - (QII+QIII) L3",                               "double",    "W",    "0"  ],
[ '158', "Max demand active power - (QII+QIII) L3 (capture time)",                "clock",     "-",    "-"  ],
[ '159', "Total Rate contract 1 Maximum demand active power + L1 (last average)", "double",    "W",    "0"  ],
[ '160', "Total Rate contract 1 Maximum demand active power + L1 (capture time)", "clock",     "-",    "-"  ],
[ '161', "Total Rate contract 1 Maximum demand active power + L2 (last average)", "double",    "W",    "0"  ],
[ '162', "Total Rate contract 1 Maximum demand active power + L2 (capture time)", "clock",     "-",    "-"  ],
[ '163', "Total Rate contract 1 Maximum demand active power + L3 (last average)", "double",    "W",    "0"  ],
[ '164', "Total Rate contract 1 Maximum demand active power + L3 (capture time)", "clock",     "-",    "-"  ],
[ '165', "Total Rate contract 1 Maximum demand active power - L1 (last average)", "double",    "W",    "0"  ],
[ '166', "Total Rate contract 1 Maximum demand active power - L1 (capture time)", "clock",     "-",    "-"  ],
[ '167', "Total Rate contract 1 Maximum demand active power - L2 (last average)", "double",    "W",    "0"  ],
[ '168', "Total Rate contract 1 Maximum demand active power - L2 (capture time)", "clock",     "-",    "-"  ],
[ '169', "Total Rate contract 1 Maximum demand active power - L3 (last average)", "double",    "W",    "0"  ],
[ '170', "Total Rate contract 1 Maximum demand active power - L3 (capture time)", "clock",     "-",    "-"  ],
[ '171', "Instantaneous Apparent power + (QI+QIV) L1",                            "double",    "VA",   "0"  ],
[ '172', "Instantaneous Apparent power - (QII+QIII) L1",                          "double",    "VA",   "0"  ],
[ '173', "Instantaneous Apparent power + (QI+QIV) L2",                            "double",    "VA",   "0"  ],
[ '174', "Instantaneous Apparent power - (QII+QIII) L2",                          "double",    "VA",   "0"  ],
[ '175', "Instantaneous Apparent power + (QI+QIV) L3",                            "double",    "VA",   "0"  ],
[ '176', "Instantaneous Apparent power - (QII+QIII) L3",                          "double",    "VA",   "0"  ],
[ '177', "Instantaneous Apparent power + (QI+QIV) (Sum of all phases)",           "double",    "VA",   "0"  ],
[ '178', "Instantaneous Apparent power - (QII+QIII) (Sum of all phases)",         "double",    "VA",   "0"  ],
[ '179', "Maximum Apparent Power per phase (S PMF )",                             "double",    "VA",   "0"  ],
[ '180', "Duration of long power failures in all phases",                         "double",    "s",    "0"  ],
[ '181', "Duration of long power failures in phase L1",                           "double",    "s",    "0"  ],
[ '182', "Duration of long power failures in phase L2",                           "double",    "s",    "0"  ],
[ '183', "Duration of long power failures in phase L3",                           "double",    "s",    "0"  ],
[ '184', "Duration of long power failures in any phase",                          "double",    "s",    "0"  ],
[ '185', "Number of long power failures in all phases",                           "long",      "-",    "-"  ],
[ '186', "Number of long power failures in phase L1",                             "long",      "-",    "-"  ],
[ '187', "Number of long power failures in phase L2",                             "long",      "-",    "-"  ],
[ '188', "Number of long power failures in phase L3",                             "long",      "-",    "-"  ],
[ '189', "Number of long power failures in any phase",                            "long",      "-",    "-"  ],
[ '190', "Number of undervoltages in any phase",                                  "long",      "-",    "-"  ],
[ '191', "Duration of undervoltages in any phase",                                "double",    "s",    "0"  ],
[ '192', "Number of undervoltages in phase L1 1",                                 "long",      "-",    "-"  ],
[ '193', "Duration of undervoltages in phase L1 1",                               "double",    "s",    "0"  ],
[ '194', "Number of undervoltages in phase L2 1",                                 "long",      "-",    "-"  ],
[ '195', "Duration of undervoltages inphase L2 1",                                "double",    "s",    "0"  ],
[ '196', "Number of undervoltages in phase L3 1",                                 "long",      "-",    "-"  ],
[ '197', "Duration of undervoltages in phase L3 1",                               "double",    "s",    "0"  ],
[ '198', "Number of undervoltages for average voltage in all 3 phases 1",         "long",      "-",    "-"  ],
[ '199', "Duration of undervoltages for average voltage in all 3 phases 1",       "double",    "s",    "0"  ],
[ '200', "Number of overvoltages in any phase",                                   "long",      "-",    "-"  ],
[ '201', "Duration of overvoltagess in any phase",                                "double",    "s",    "0"  ],
[ '202', "Number of overvoltages in phase L1 1",                                  "long",      "-",    "-"  ],
[ '203', "Duration of overvoltages in phase L1 1",                                "double",    "s",    "0"  ],
[ '204', "Number of overvoltages in phase L2 1",                                  "long",      "-",    "-"  ],
[ '205', "Duration of overvoltages in phase L2 1",                                "double",    "s",    "0"  ],
[ '206', "Number of overvoltages in phase L3 1",                                  "long",      "-",    "-"  ],
[ '207', "Duration of overvoltages in phase L3 1",                                "double",    "s",    "0"  ],
[ '208', "Number of overvoltages for average voltage in all 3 phases 1",          "long",      "-",    "-"  ],
[ '209', "Duration of overvoltages for average voltage in all 3 phases 1",        "double",    "s",    "0"],
[ '210', "Not described in the manual", "X", "-", "0"],
[ '211', "Not described in the manual", "X", "-", "0"],
[ '212', "Not described in the manual", "X", "-", "0"],
[ '213', "Not described in the manual", "X", "-", "0"],
[ '214', "Not described in the manual", "X", "-", "0"],
[ '215', "Not described in the manual", "X", "-", "0"],
[ '216', "Not described in the manual", "X", "-", "0"],
[ '217', "Not described in the manual", "X", "-", "0"],
[ '218', "Not described in the manual", "X", "-", "0"],
[ '219', "Not described in the manual", "X", "-", "0"],
[ '220', "Not described in the manual", "X", "-", "0"],
[ '221', "Not described in the manual", "X", "-", "0"],
[ '222', "Not described in the manual", "X", "-", "0"],
[ '223', "Not described in the manual", "X", "-", "0"],
[ '224', "Not described in the manual", "X", "-", "0"],
[ '225', "Not described in the manual", "X", "-", "0"],
[ '226', "Not described in the manual", "X", "-", "0"],
[ '227', "Not described in the manual", "X", "-", "0"],
[ '228', "Not described in the manual", "X", "-", "0"],
[ '229', "Not described in the manual", "X", "-", "0"],
[ '230', "Not described in the manual", "X", "-", "0"],
[ '231', "Not described in the manual", "X", "-", "0"],
[ '232', "Not described in the manual", "X", "-", "0"],
[ '233', "Not described in the manual", "X", "-", "0"],
[ '234', "Not described in the manual", "X", "-", "0"],
[ '235', "Not described in the manual", "X", "-", "0"],
[ '236', "Not described in the manual", "X", "-", "0"],
[ '237', "Not described in the manual", "X", "-", "0"],
[ '238', "Not described in the manual", "X", "-", "0"],
[ '239', "Not described in the manual", "X", "-", "0"],
[ '240', "Not described in the manual", "X", "-", "0"],
[ '241', "Not described in the manual", "X", "-", "0"],
[ '242', "Not described in the manual", "X", "-", "0"],
[ '243', "Not described in the manual", "X", "-", "0"],
[ '244', "Not described in the manual", "X", "-", "0"],
[ '245', "Not described in the manual", "X", "-", "0"],
[ '246', "Not described in the manual", "X", "-", "0"],
[ '247', "Not described in the manual", "X", "-", "0"],
[ '248', "Not described in the manual", "X", "-", "0"],
[ '249', "Not described in the manual", "X", "-", "0"],
[ '250', "Not described in the manual", "X", "-", "0"],
[ '251', "Not described in the manual", "X", "-", "0"],
[ '252', "Not described in the manual", "X", "-", "0"],
[ '253', "Not described in the manual", "X", "-", "0"],
[ '254', "Not described in the manual", "X", "-", "0"],
[ '255', "Not described in the manual", "X", "-", "0"]]

# configure CRC calculation
crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)

############################################################
HOST = '127.0.0.1'   # The remote host
PORT = 3000          # The port to connect to
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.connect((HOST, PORT))
############################################################

# function to add CRC to command
def add_crc(data):
    # get CRC and return it in hex with 4 digits
    crc = "0x{:04x}".format((crc16(bytearray.fromhex(data))))
    return(data + crc[4:6] + crc[2:4])

# function to get registers
def get_data(data):
    cmd = bytearray.fromhex(add_crc(data))  # add CRC to the command
    got = 1                                 # main loop, get data
    while got:                              # loop until get valid response to command
        ser.sendall(cmd)                    # write request to serial
        time.sleep(0.8)                     # wait a while before reading modbus response...
        resp = ser.recv(1).hex()            # read 1 byte from the socket
        c = 0                               # counter to prevent looping forever
        while resp != data[0:2]:            # check up to 32 bytes if response comes from the right slave
            resp = ser.recv(1).hex()        # if not, keep reading serial buffer
            c += 1                          # prevent looping forever
            if c == 32:                     # there was a loop, start from beginning
                break
        resp = resp + ser.recv(1).hex()     # possibly found slave number response corret so add the comand and check it
        if resp == "0104":                  # break the loop if the response includes the requested sent command
            resp = resp + ser.recv(1).hex()        # get how many bytes are there to retrieve
            get_more = int(resp[4:6], 16) + 2      # set the number of additional bytes to read and do it, includding CRC
            resp = resp + ser.recv(get_more).hex() # get the remaining data
            crc = crc16(bytearray.fromhex(resp))   # check CRC response sanity
            if crc == 0:                           # check if CRC is ok
                got = 0                            # got good data, break the main get data loop and return data
        if resp == "01c5" or resp == "0184":       # if it was not a "04" command response, check if it was an exception
            resp = resp + ser.recv(6).hex()        # if so, get the exception number
            crc = crc16(bytearray.fromhex(resp))   # check CRC response sanity
            error = "Unknown error code: "
            if crc == 0:                           # check if CRC is ok
                x = resp[4:6]
                if x == "01":
                    error = "Illigal function. Error code: "
                if x == "02":
                    error = "Illigal address. Error code: "
                if x == "03":
                    error = "Illigal data values. Error code: "
                if x == "04":
                    error = "Slave device failure. Error code: "
                if x == "81":
                    error = "Access denied. Error code: "
                if x == "82":
                    error = "Measurement does not exist. Error code: "
                if x == "83":
                    error = "Entry does not exist. Error code: "
                if x == "84":
                    error = "Data to retrieve exceeded. Error code: "
            ser.close()
            sys.exit(error + resp)
    ser.close()                              # close socket
    return(resp)                             # return colected response

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("This script reads only one register at a time.")
    print("I.e. ./TCP_read_register.py 1")
    sys.exit(-1)

# get the register to be read from command line
cmd = int(sys.argv[1])

# define the kind of requested data
name_   = cmd_04[cmd][1]              # get register name
type_   = cmd_04[cmd][2]              # get register type
unit_   = cmd_04[cmd][3]              # get register unity
scaler_ = cmd_04[cmd][4]              # get register scale

if scaler_ != "-":                    # if there is a scaler, then process it
    base_   = 10 ** abs(int(scaler_)) # get the number of decimal places
    if base_ == 0:                    # Avoid division by zero
        base_ = 1

# print initial data about the request
print("{:0>3d}".format(cmd) + "," + name_ + "," + type_ + "," + unit_ + "," + scaler_ + ",", end='')

# build hex command to be sent over serial port
hex_cmd = "0104" + "{:04x}".format(cmd) + "0001"

resp = get_data(hex_cmd)   # get data
reg  = []                  # set array to receive extrated data

# process data based on byte size/type
######################################

# if long
if type_ == "long":        # process long size
    reg.append(int(resp[6:10],  16))

# if double
if type_ == "double":      # process double size
    reg.append(int(resp[6:14],  16))

# if clock
if type_ == "clock":       # process clock
    reg.append(int(resp[6:10],  16)) # reg-0  Year
    reg.append(int(resp[10:12], 16)) # reg-1  Month
    reg.append(int(resp[12:14], 16)) # reg-2  Day
    reg.append(int(resp[14:16], 16)) # reg-3  weekday
    reg.append(int(resp[16:18], 16)) # reg-4  Hour
    reg.append(int(resp[18:20], 16)) # reg-5  Mimutes
    reg.append(int(resp[20:22], 16)) # reg-6  Seconds
    reg.append(int(resp[22:24], 16)) # reg-7  Hunderds of seconds
    reg.append(int(resp[24:28], 16)) # reg-8  Deviation from local to GMT
    reg.append(int(resp[28:30], 16)) # reg-9  Clock status (0x0* Winter; 0x8* Summer; 0FF not specified)

    if reg[8] == 32768:     # process GMT
        reg[8] = "Not specified"
    else: reg[8] = str(reg[8])

    if reg[9]  < 8:         # process season
        reg[9] = "Winter"
    if reg[9]  > 7:
        reg[9] = "Summer"
    if reg[9]  == 255:
        reg[9] = "Not epecified"

    print(str(reg[0]) + "-" + str(reg[1]) + "-" + str(reg[2]), end='')
    print(" " + str(reg[4]) + ":" + str(reg[5]) + ":" + str(reg[6]))
#    print("GMT distance: " + reg[8])
#    print("Weekday: " + str(reg[3]) + "\nClock status: " + reg[9])
    sys.exit(0)

if type_ == "unsigned":    # process unsigned
    reg.append(int(resp[6:8],  16))

######## TO BE DONE ###########################
###############################################
if type_ == "array":  # process disconnect
    print(resp + ", not parsed")
    sys.exit()

if type_ == "disconnect":  # process disconnect
    print(resp + ", not parsed")
    sys.exit()

if type_ == "octet":       # process octect
    print(resp + ", not parsed")
    sys.exit()

if type_ == "bitString":   # process bitString
    print(resp + ", not parsed")
    sys.exit()

if type_ == "demand":  # process disconnect
    print(resp + ", not parsed")
    sys.exit()
######## END OF TO BE DONE ####################
###############################################

# prepare for generic printing results
######################################

if scaler_ != "-":         # if there is a scaler
    reg[0] = reg[0]/base_  # apply scaler

if unit_ == "-":           # if there is no unity, remove "-" from it
    unit_ = ""

# print generic data
print(str(reg[0]))

sys.exit(0)
