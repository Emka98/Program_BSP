mass = 625
We = mass * 2.20462262
np = 500
v_max_ms = 62
v_max = v_max_ms * 1.944
T_max = 145_000

text_1986 = ""
text_1970 = ""

# rozwoj konstrukcji w 1986 [h]
c1_1970 = 0.027
c2_1970= 0.791
c3_1970 = 1.526
c4_1970 = 0.183

c1_1986 = 4.86
c2_1986= 0.777
c3_1986 = 0.894
c4_1986 = 0.163

He_1986 = c1_1986 * We**c2_1986 * v_max**c3_1986 * np**c4_1986
He_1970 = c1_1970 * We**c2_1970 * v_max**c3_1970 * np**c4_1970

wspolny_text = "Czas na rozwój konstrukcji: "
text_1986 += wspolny_text + str(He_1986) + "h" + "\n"
text_1970 += wspolny_text + str(He_1970) + "h" + "\n"

# Wsparcie prac badawczo rozwojowych [USD]
c1_1970 = 0.00549
c2_1970 = 0.873
c3_1970 = 1.890
c4_1970 = 0.346

c1_1986 = 45.42
c2_1986 = 0.63
c3_1986 = 1.3
c4_1986 = 0

Cd_1986 = c1_1986 * We **c2_1986 * v_max**c3_1986 * np**c4_1986
Cd_1970 = c1_1970 * We **c2_1970 * v_max**c3_1970 * np**c4_1970

wspolny_text = "Wsparcie prac badawczo rozwojowych: "
text_1970 += wspolny_text + str(Cd_1970) + "USD" + "\n"
text_1986 += wspolny_text + str(Cd_1986) + "USD" + "\n"

# Cena silnika i awioniki [USD]
c1_1970 = 130
c2_1970 = 0.836

c1_1986 = 1548.0
c2_1986 = 0.04324
c3_1986 = 3.25
c4_1986 = 0.969
c5_1986 = 2228.0

Cen_1970 = c1_1970 * T_max**c2_1970
Cen_1986 = c1_1986 * (c2_1986 * T_max)


# Robocizna 
Cen_1986 = c1_1986 * We **c1_1986 * v_max**c3_1986 * np**c4_1986
print("Rok 1970:")
print(text_1970)
print("Rok 1986:")
print(text_1986)
