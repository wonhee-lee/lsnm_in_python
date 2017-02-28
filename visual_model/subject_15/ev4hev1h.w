% Thu Nov 19 22:10:16 2015

% Input layer: (9, 9)
% Output layer: (9, 9)
% Fanout size: (1, 5)
% Fanout spacing: (1, 1)
% Specified fanout weights

Connect(ev4h, ev1h)  {
  From:  (1, 1)  {
    |              |     ([ 1, 9]  0.001146)     ([ 1, 1]  0.001736)     ([ 1, 2]  0.001355)     ([ 1, 3]  0.001992) 
  }
  From:  (1, 2)  {
    |              |     |              |     |              |     |              |     ([ 1, 4]  0.000756) 
  }
  From:  (1, 3)  {
    |              |     |              |     |              |     |              |     ([ 1, 5]  0.000618) 
  }
  From:  (1, 4)  {
    |              |     ([ 1, 3]  0.000056)     |              |     |              |     |              | 
  }
  From:  (1, 5)  {
    ([ 1, 3]  0.001448)     ([ 1, 4]  0.000411)     |              |     ([ 1, 6]  0.000202)     ([ 1, 7]  0.000850) 
  }
  From:  (1, 6)  {
    |              |     |              |     |              |     |              |     |              | 
    ([ 1, 1]  0.001602)   }
  From:  (1, 7)  {
    ([ 1, 5]  0.000172)     ([ 1, 6]  0.001544)     ([ 1, 7]  0.000103)     |              |     |              | 
  }
  From:  (1, 8)  {
    ([ 1, 6]  0.000624)     ([ 1, 7]  0.001980)     ([ 1, 8]  0.000939)     |              |     ([ 1, 1]  0.001935) 
  }
  From:  (1, 9)  {
    |              |     ([ 1, 8]  0.000946)     |              |     |              |     ([ 1, 2]  0.001800) 
  }
  From:  (2, 1)  {
    |              |     ([ 2, 9]  0.001350)     |              |     ([ 2, 2]  0.000584)     ([ 2, 3]  0.001915) 
  }
  From:  (2, 2)  {
    ([ 2, 9]  0.001962)     ([ 2, 1]  0.000475)     ([ 2, 2]  0.001210)     ([ 2, 3]  0.000419)     ([ 2, 4]  0.000388) 
  }
  From:  (2, 3)  {
    ([ 2, 1]  0.000898)     |              |     ([ 2, 3]  0.001584)     |              |     |              | 
  }
  From:  (2, 4)  {
    |              |     ([ 2, 3]  0.001895)     |              |     ([ 2, 5]  0.001136)     ([ 2, 6]  0.000009) 
  }
  From:  (2, 5)  {
    |              |     |              |     ([ 2, 5]  0.000132)     ([ 2, 6]  0.001109)     ([ 2, 7]  0.001992) 
  }
  From:  (2, 6)  {
    ([ 2, 4]  0.000187)     ([ 2, 5]  0.000273)     |              |     ([ 2, 7]  0.001125)     ([ 2, 8]  0.001775) 
  }
  From:  (2, 7)  {
    ([ 2, 5]  0.001223)     ([ 2, 6]  0.001262)     ([ 2, 7]  0.001724)     |              |     ([ 2, 9]  0.001836) 
  }
  From:  (2, 8)  {
    |              |     |              |     |              |     ([ 2, 9]  0.000560)     ([ 2, 1]  0.000152) 
  }
  From:  (2, 9)  {
    ([ 2, 7]  0.001962)     |              |     |              |     ([ 2, 1]  0.000594)     |              | 
  }
  From:  (3, 1)  {
    ([ 3, 8]  0.000235)     ([ 3, 9]  0.000096)     |              |     ([ 3, 2]  0.001994)     |              | 
  }
  From:  (3, 2)  {
    |              |     ([ 3, 1]  0.001733)     |              |     ([ 3, 3]  0.001302)     ([ 3, 4]  0.001534) 
  }
  From:  (3, 3)  {
    |              |     ([ 3, 2]  0.000506)     |              |     |              |     ([ 3, 5]  0.001107) 
  }
  From:  (3, 4)  {
    |              |     |              |     ([ 3, 4]  0.000618)     ([ 3, 5]  0.000001)     |              | 
  }
  From:  (3, 5)  {
    ([ 3, 3]  0.001262)     |              |     ([ 3, 5]  0.000490)     ([ 3, 6]  0.000506)     ([ 3, 7]  0.001314) 
  }
  From:  (3, 6)  {
    |              |     ([ 3, 5]  0.000123)     |              |     ([ 3, 7]  0.001762)     |              | 
  }
  From:  (3, 7)  {
    ([ 3, 5]  0.000185)     ([ 3, 6]  0.001583)     |              |     |              |     ([ 3, 9]  0.000057) 
  }
  From:  (3, 8)  {
    ([ 3, 6]  0.000298)     ([ 3, 7]  0.001540)     |              |     ([ 3, 9]  0.001136)     |              | 
  }
  From:  (3, 9)  {
    |              |     |              |     ([ 3, 9]  0.001532)     |              |     |              | 
  }
  From:  (4, 1)  {
    ([ 4, 8]  0.001975)     ([ 4, 9]  0.000162)     |              |     ([ 4, 2]  0.000055)     ([ 4, 3]  0.000385) 
  }
  From:  (4, 2)  {
    ([ 4, 9]  0.000110)     |              |     |              |     |              |     ([ 4, 4]  0.001089) 
  }
  From:  (4, 3)  {
    |              |     |              |     |              |     |              |     |              | 
    ([ 1, 1]  0.001260)   }
  From:  (4, 4)  {
    |              |     |              |     ([ 4, 4]  0.001101)     |              |     ([ 4, 6]  0.000950) 
  }
  From:  (4, 5)  {
    |              |     ([ 4, 4]  0.001984)     |              |     ([ 4, 6]  0.000843)     |              | 
  }
  From:  (4, 6)  {
    |              |     ([ 4, 5]  0.000988)     |              |     |              |     ([ 4, 8]  0.000871) 
  }
  From:  (4, 7)  {
    ([ 4, 5]  0.000325)     ([ 4, 6]  0.001122)     ([ 4, 7]  0.001399)     |              |     |              | 
  }
  From:  (4, 8)  {
    ([ 4, 6]  0.000444)     ([ 4, 7]  0.000494)     |              |     ([ 4, 9]  0.000538)     |              | 
  }
  From:  (4, 9)  {
    |              |     |              |     |              |     ([ 4, 1]  0.000583)     ([ 4, 2]  0.000509) 
  }
  From:  (5, 1)  {
    ([ 5, 8]  0.001089)     |              |     ([ 5, 1]  0.001191)     ([ 5, 2]  0.000672)     |              | 
  }
  From:  (5, 2)  {
    |              |     ([ 5, 1]  0.001296)     |              |     |              |     ([ 5, 4]  0.000787) 
  }
  From:  (5, 3)  {
    ([ 5, 1]  0.001014)     |              |     |              |     |              |     ([ 5, 5]  0.000782) 
  }
  From:  (5, 4)  {
    |              |     |              |     ([ 5, 4]  0.001686)     |              |     ([ 5, 6]  0.000070) 
  }
  From:  (5, 5)  {
    ([ 5, 3]  0.000745)     ([ 5, 4]  0.000295)     |              |     |              |     |              | 
  }
  From:  (5, 6)  {
    ([ 5, 4]  0.001849)     |              |     ([ 5, 6]  0.001880)     ([ 5, 7]  0.000020)     |              | 
  }
  From:  (5, 7)  {
    ([ 5, 5]  0.000994)     |              |     ([ 5, 7]  0.000217)     |              |     |              | 
  }
  From:  (5, 8)  {
    |              |     |              |     ([ 5, 8]  0.000105)     ([ 5, 9]  0.001925)     |              | 
  }
  From:  (5, 9)  {
    ([ 5, 7]  0.000399)     |              |     |              |     |              |     ([ 5, 2]  0.001158) 
  }
  From:  (6, 1)  {
    ([ 6, 8]  0.000588)     ([ 6, 9]  0.000740)     |              |     |              |     ([ 6, 3]  0.000978) 
  }
  From:  (6, 2)  {
    |              |     ([ 6, 1]  0.000487)     ([ 6, 2]  0.001405)     |              |     |              | 
  }
  From:  (6, 3)  {
    |              |     |              |     ([ 6, 3]  0.001002)     |              |     ([ 6, 5]  0.001661) 
  }
  From:  (6, 4)  {
    |              |     ([ 6, 3]  0.001986)     |              |     |              |     |              | 
  }
  From:  (6, 5)  {
    |              |     ([ 6, 4]  0.000702)     ([ 6, 5]  0.000666)     ([ 6, 6]  0.001426)     ([ 6, 7]  0.000337) 
  }
  From:  (6, 6)  {
    |              |     ([ 6, 5]  0.001429)     ([ 6, 6]  0.001170)     ([ 6, 7]  0.000933)     ([ 6, 8]  0.001363) 
  }
  From:  (6, 7)  {
    |              |     ([ 6, 6]  0.001370)     ([ 6, 7]  0.000308)     ([ 6, 8]  0.000521)     |              | 
  }
  From:  (6, 8)  {
    ([ 6, 6]  0.001712)     |              |     ([ 6, 8]  0.000539)     |              |     ([ 6, 1]  0.000111) 
  }
  From:  (6, 9)  {
    |              |     |              |     |              |     |              |     ([ 6, 2]  0.000596) 
  }
  From:  (7, 1)  {
    ([ 7, 8]  0.001935)     ([ 7, 9]  0.001225)     |              |     ([ 7, 2]  0.001078)     ([ 7, 3]  0.001790) 
  }
  From:  (7, 2)  {
    |              |     ([ 7, 1]  0.001952)     ([ 7, 2]  0.000835)     |              |     ([ 7, 4]  0.000431) 
  }
  From:  (7, 3)  {
    ([ 7, 1]  0.000407)     |              |     |              |     ([ 7, 4]  0.000004)     |              | 
  }
  From:  (7, 4)  {
    |              |     ([ 7, 3]  0.000075)     ([ 7, 4]  0.001530)     |              |     |              | 
  }
  From:  (7, 5)  {
    |              |     ([ 7, 4]  0.000609)     |              |     ([ 7, 6]  0.001128)     ([ 7, 7]  0.000890) 
  }
  From:  (7, 6)  {
    |              |     |              |     ([ 7, 6]  0.001021)     |              |     ([ 7, 8]  0.001486) 
  }
  From:  (7, 7)  {
    ([ 7, 5]  0.001071)     |              |     |              |     ([ 7, 8]  0.000908)     ([ 7, 9]  0.001539) 
  }
  From:  (7, 8)  {
    ([ 7, 6]  0.001739)     |              |     ([ 7, 8]  0.000332)     ([ 7, 9]  0.001837)     |              | 
  }
  From:  (7, 9)  {
    |              |     ([ 7, 8]  0.000707)     |              |     |              |     ([ 7, 2]  0.001383) 
  }
  From:  (8, 1)  {
    ([ 8, 8]  0.000010)     |              |     |              |     ([ 8, 2]  0.000478)     ([ 8, 3]  0.000375) 
  }
  From:  (8, 2)  {
    |              |     |              |     |              |     ([ 8, 3]  0.000582)     ([ 8, 4]  0.000995) 
  }
  From:  (8, 3)  {
    |              |     |              |     |              |     |              |     |              | 
    ([ 1, 1]  0.001797)   }
  From:  (8, 4)  {
    ([ 8, 2]  0.001906)     |              |     ([ 8, 4]  0.000617)     |              |     ([ 8, 6]  0.001867) 
  }
  From:  (8, 5)  {
    |              |     ([ 8, 4]  0.001029)     ([ 8, 5]  0.001544)     ([ 8, 6]  0.001216)     |              | 
  }
  From:  (8, 6)  {
    |              |     |              |     |              |     ([ 8, 7]  0.000740)     ([ 8, 8]  0.001287) 
  }
  From:  (8, 7)  {
    |              |     |              |     |              |     |              |     ([ 8, 9]  0.001933) 
  }
  From:  (8, 8)  {
    |              |     |              |     |              |     |              |     ([ 8, 1]  0.001267) 
  }
  From:  (8, 9)  {
    ([ 8, 7]  0.000743)     ([ 8, 8]  0.001544)     ([ 8, 9]  0.000678)     |              |     ([ 8, 2]  0.001270) 
  }
  From:  (9, 1)  {
    |              |     |              |     |              |     ([ 9, 2]  0.000010)     ([ 9, 3]  0.001156) 
  }
  From:  (9, 2)  {
    |              |     |              |     ([ 9, 2]  0.000894)     |              |     ([ 9, 4]  0.001269) 
  }
  From:  (9, 3)  {
    |              |     |              |     |              |     |              |     ([ 9, 5]  0.000572) 
  }
  From:  (9, 4)  {
    |              |     ([ 9, 3]  0.001015)     |              |     ([ 9, 5]  0.000718)     |              | 
  }
  From:  (9, 5)  {
    |              |     ([ 9, 4]  0.001864)     ([ 9, 5]  0.001222)     |              |     |              | 
  }
  From:  (9, 6)  {
    ([ 9, 4]  0.001571)     ([ 9, 5]  0.000185)     |              |     |              |     |              | 
  }
  From:  (9, 7)  {
    |              |     ([ 9, 6]  0.001459)     ([ 9, 7]  0.000700)     |              |     |              | 
  }
  From:  (9, 8)  {
    |              |     ([ 9, 7]  0.001085)     |              |     ([ 9, 9]  0.000213)     |              | 
  }
  From:  (9, 9)  {
    ([ 9, 7]  0.001704)     ([ 9, 8]  0.001276)     |              |     ([ 9, 1]  0.001626)     |              | 
  }
}