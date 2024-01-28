'''
Calculates:
    Damage per shot
    DPS
    DPS with reload time
for various weapons. You can compare Rivens here if you are not sure which one is better with different mods used.

To add new weapon into DB uncomment  # add_weapon() and edit setting for that def.

Note is not saved in pickle. It is saved at the bottom of this code.
'''
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import pickle

# -------------- VARIABLES ---------------------------------------
if True:
    name = ''
    accuracy = ''
    crit_chance = ''
    crit_multip = ''
    fire_rate = ''
    magazine = ''
    noise = ''
    reload = ''
    status = ''
    impact = ''
    puncture = ''
    slash = ''
    elem = ''
    multishot = ''
    w_dmg_buff = 1

    m_accuracy = 1
    m_crit_chance = 1
    m_crit_multip = 1
    m_fire_rate = 1
    m_magazine = 1
    m_noise = 1
    m_reload = 1
    m_status = 1
    m_impact = 1
    m_puncture = 1
    m_slash = 1
    m_elem = 0
    m_multishot = 1
    m_dmg = 1

    t_accuracy = 0
    t_crit_chance = 0
    t_crit_multip = 0
    t_fire_rate = 0
    t_magazine = 0
    t_noise = 0
    t_reload = 0
    t_status = 0
    t_impact = 0
    t_puncture = 0
    t_slash = 0
    t_elem = 0
    t_multishot = 0


def save_pickle(path, data1):
    pkl_file = open('Pickles/' + path + '.pkl', 'wb')
    pickle.dump(data1, pkl_file)
    # Pickle the list using the highest protocol available.
    # pickle.dump(data1, output, -1)
    pkl_file.close()


def load_pickle(path):
    try:
        pkl_file = open('Pickles/' + path + '.pkl', 'rb')
        data1 = pickle.load(pkl_file)
        # pprint.pprint(data1)
    except:
        pkl_file = open(path, 'wb')
        data1 = ''
    pkl_file.close()
    return data1


def add_weapon():
    weapons = load_pickle('wf_weapons')
    # weapons = {}
    name = 'Nami Skyla Prime'
    accuracy = 100
    crit_chance = 0.22
    crit_multip = 2
    fire_rate = 1.33
    magazine = 1
    noise = 'silent'
    reload = 0
    status = 0.34
    impact = 18
    slash = 126
    puncture = 36
    elem = 0
    # w_dmg_buff = 1  # in simulacrum
    weapons[name] = {'accuracy': accuracy, 'crit_chance': crit_chance, 'crit_multip': crit_multip,
                     'fire_rate': fire_rate, 'magazine': magazine, 'noise': noise, 'reload': reload, 'status': status,
                     'impact': impact, 'puncture': puncture, 'slash': slash, 'elem': elem, 'multishot': multishot,
                     'w_dmg_buff': w_dmg_buff}
    # del weapons['Rubico (Scoped) +50%dmg + 50%crit dmg']
    save_pickle('wf_weapons', weapons)


# add_weapon()


def apply_mods():
    global m_accuracy
    global m_crit_chance
    global m_crit_multip
    global m_fire_rate
    global m_magazine
    global m_noise
    global m_reload
    global m_status
    global m_impact
    global m_puncture
    global m_slash
    global m_elem
    global m_multishot
    global m_dmg
    global w_dmg_buff

    m_accuracy = 1
    m_crit_chance = 1
    m_crit_multip = 1
    m_fire_rate = 1
    m_magazine = 1
    m_noise = 1
    m_reload = 1
    m_status = 1
    m_impact = 1
    m_puncture = 1
    m_slash = 1
    m_elem = 0
    m_multishot = 1
    m_dmg = 1

    # 60 60 element status mods
    if electric6060.get() == 1:
        m_elem += 0.6
        m_status += 0.6
    if toxin6060.get() == 1:
        m_elem += 0.6
        m_status += 0.6
    if cold6060.get() == 1:
        m_elem += 0.6
        m_status += 0.6
    if heat6060.get() == 1:
        m_elem += 0.6
        m_status += 0.6
    if electric90.get() == 1:
        m_elem += 0.9
    if toxin90.get() == 1:
        m_elem += 0.9
    if cold90.get() == 1:
        m_elem += 0.9
    if heat90.get() == 1:
        m_elem += 0.9

    if vigilante_armaments.get() == 1:
        m_multishot += 0.6

    # Rifle
    if serration.get() == 1:
        m_dmg += 1.65
    if split_chamber.get() == 1:
        m_multishot += 0.9
    if point_strike.get() == 1:
        m_crit_chance += 1.5
    if vital_sense.get() == 1:
        m_crit_multip += 1.2
    if heavy_caliber.get() == 1:
        m_dmg += 1.65  # 1.05
        m_accuracy -= 0.55  # 0.35
    if p_cryo_rounds.get() == 1:
        m_elem += 1.65  # 1.05

    if crash_course.get() == 1:
        m_impact += 1.2

    if critical_dealy.get() == 1:
        m_crit_chance += 0.48
        m_fire_rate -= 0.36
    if hammer_shot.get() == 1:
        m_crit_multip += 0.6
        m_status += 0.4
    if wildfire.get() == 1:
        m_elem += 0.6
        m_magazine += 0.2
    if speed_trigger.get() == 1:
        m_fire_rate += 0.6
    if vile_acceleration.get() == 1:
        m_fire_rate += 0.9
        m_dmg -= 0.15

    # Shotgun
    if p_point_blank.get() == 1:
        m_dmg += 1.65 - 0.0165
    if hells_chamber.get() == 1:
        m_multishot += 1.2
    if blaze.get() == 1:
        m_dmg += 0.6
        m_elem += 0.6
    if p_charged_shell.get() == 1:
        m_elem += 1.5
    if chilling_reload.get() == 1:
        m_elem += 0.6
        m_reload += 0.4
    if ammo_stock.get() == 1:
        m_magazine += 0.6

    # Melee
    if p_fevr_strike.get() == 1:
        m_elem += 1.65
    if sacrf_steel.get() == 1:
        m_crit_chance += 2.2
    if p_pressure_point.get() == 1:
        m_dmg += 1.65
    if spoiled_strike.get() == 1:
        m_dmg += 1
        m_fire_rate -= 0.2
    if organ_shatter.get() == 1:
        m_crit_multip += 0.9
    if true_steel.get() == 1:
        m_crit_chance += 1.2
    if gladiator_might.get() == 1:
        m_crit_multip += 0.6

    if apply_riven1.get() == 1:
        try:
            x = float(r_heat.get()) + float(r_electricity.get()) + float(r_cold.get()) + float(r_toxin.get())
            m_elem += x
        except:
            pass
        try:
            x = float(r_multishot.get())
            m_multishot += x
        except:
            pass
        try:
            x = float(r_crit_dmg.get())
            m_crit_multip += x
        except:
            pass
        try:
            x = float(r_damage.get())
            m_dmg += x
        except:
            pass
        try:
            x = float(r_status.get())
            m_status += x
        except:
            pass
        try:
            x = float(r_slash.get())
            m_slash += x
        except:
            pass
        try:
            x = float(r_impact.get())
            m_impact += x
        except:
            pass
        try:
            x = float(r_puncture.get())
            m_puncture += x
        except:
            pass
        try:
            x = float(r_crit_chance.get())
            m_crit_chance += x
        except:
            pass
        try:
            x = float(r_reload.get())
            m_reload += x
        except:
            pass
        try:
            x = float(r_magazine.get())
            m_magazine += x
        except:
            pass
        try:
            x = float(r_fire_rate.get())
            m_fire_rate += x
        except:
            pass

        try:
            x = float(chroma_buff.get())
            m_dmg += x
        except:
            pass

    if apply_riven2.get() == 1:
        try:
            x = float(r2_heat.get()) + float(r2_electricity.get()) + float(r2_cold.get()) + float(r2_toxin.get())
            m_elem += x
        except:
            pass
        try:
            x = float(r2_multishot.get())
            m_multishot += x
        except:
            pass
        try:
            x = float(r2_crit_dmg.get())
            m_crit_multip += x
        except:
            pass
        try:
            x = float(r2_damage.get())
            m_dmg += x
        except:
            pass
        try:
            x = float(r2_status.get())
            m_status += x
        except:
            pass
        try:
            x = float(r2_slash.get())
            m_slash += x
        except:
            pass
        try:
            x = float(r2_impact.get())
            m_impact += x
        except:
            pass
        try:
            x = float(r2_puncture.get())
            m_puncture += x
        except:
            pass
        try:
            x = float(r2_crit_chance.get())
            m_crit_chance += x
        except:
            pass
        try:
            x = float(r2_reload.get())
            m_reload += x
        except:
            pass
        try:
            x = float(r2_magazine.get())
            m_magazine += x
        except:
            pass
        try:
            x = float(r2_fire_rate.get())
            m_fire_rate += x
        except:
            pass
        try:
            x = float(chroma_buff2.get())
            m_dmg += x
        except:
            pass

    # m_dmg = ((m_dmg - 1) * w_dmg_buff) + 1  # Simulacrum fucked up
    pick_weapon('')
    return True


def calculator():
    global t_accuracy
    global t_crit_chance
    global t_crit_multip
    global t_fire_rate
    global t_magazine
    global t_noise
    global t_reload
    global t_status
    global t_impact
    global t_puncture
    global t_slash
    global t_elem
    global t_multishot

    multishot = 1
    t_multishot = multishot * m_multishot
    base_elem = impact + puncture + slash + elem
    t_accuracy = accuracy * m_accuracy
    t_crit_chance = crit_chance * m_crit_chance
    t_crit_multip = crit_multip * m_crit_multip
    t_fire_rate = fire_rate * m_fire_rate
    t_magazine = round(magazine * m_magazine)
    t_noise = noise * m_noise
    t_reload = reload / m_reload
    # t_status = status * m_status
    t_status = 1 - (1 - (status * m_status)) ** t_multishot
    try:
        t_status = round(t_status*100, 1)
    except:
        t_status = 100

    t_impact = impact * m_impact * t_multishot * m_dmg
    t_puncture = puncture * m_puncture * t_multishot * m_dmg
    t_slash = slash * m_slash * t_multishot * m_dmg
    # t_elem = elem * m_elem
    t_elem = (base_elem * m_elem + elem) * t_multishot * m_dmg

    dmg_sum = t_elem + t_impact + t_puncture + t_slash
    dmg_p_crit = dmg_sum * ((1 - t_crit_chance) + t_crit_chance * t_crit_multip)
    dps = dmg_p_crit * t_fire_rate
    dps_reload = (t_magazine / t_fire_rate) / ((t_magazine / t_fire_rate) + t_reload) * dps

    s = 'accuracy ' + str(round(m_accuracy, 2)) + "\n" + 'crit_chance ' + str(m_crit_chance) + "\n" + 'crit_multip ' + \
        str(round(m_crit_multip, 2)) + "\n" + 'fire_rate ' + str(m_fire_rate) + "\n" + 'magazine ' + str(
        m_magazine) + "\n" + 'reload ' + str(m_reload) + "\n" + 'status ' + str(
        round(m_status, 2)) + "\n" + 'impact ' + str(m_impact) + "\n" + 'slash ' + str(m_slash) + "\n" + 'puncture ' + \
        str(m_puncture) + "\n" + 'elem ' + str(round(m_elem, 2)) + "\n" + \
        'multishot ' + str(round(m_multishot, 2)) + '\n' + 'dmg ' + str(m_dmg) + '\n\n'
    w_multipl_window.delete(0.0, END)
    w_multipl_window.insert(END, s)

    s = 'accuracy ' + str(round(t_accuracy, 2)) + "\n" + 'crit_chance ' + str(round(t_crit_chance, 3)) + "\n" + \
        'crit_multip ' + str(round(t_crit_multip, 1)) + "\n" + 'fire_rate ' + str(t_fire_rate) + "\n" + 'magazine ' + \
        str(t_magazine) + "\n" + 'reload ' + str(round(t_reload, 1)) + "\n" + 'status ' + str(t_status) + \
        "\n" + 'impact ' + str(round(t_impact, 1)) + "\n" + 'slash ' + str(round(t_slash, 1)) + "\n" + 'puncture ' + \
        str(round(t_puncture, 1)) + "\n" + 'elem ' + str(round(t_elem, 1)) + '\n\n'
    w_full_window.delete(0.0, END)
    w_full_window.insert(END, s)

    s = 'dmg_sum ' + str(round(dmg_sum, 2)) + '\n' + 'dmg+crit ' + str(round(dmg_p_crit, 2)) + '\n' + 'dps ' + str(
        round(dps, 2)) + '\n' + 'dps_rel ' + str(round(dps_reload, 2))
    w_full_window.insert(END, s)


def pick_weapon(event):
    selected_weapon = cbx_selected_weapon.get()
    w = weapons[selected_weapon]
    global accuracy
    global crit_chance
    global crit_multip
    global fire_rate
    global magazine
    global noise
    global reload
    global status
    global impact
    global puncture
    global slash
    global elem
    global multishot
    global w_dmg_buff
    accuracy = w['accuracy']
    crit_chance = w['crit_chance']
    crit_multip = w['crit_multip']
    fire_rate = w['fire_rate']
    magazine = w['magazine']
    noise = w['noise']
    reload = w['reload']
    status = w['status']
    impact = w['impact']
    puncture = w['puncture']
    slash = w['slash']
    elem = w['elem']
    multishot = w['multishot']
    w_dmg_buff = w['w_dmg_buff']

    s = 'accuracy ' + str(w['accuracy']) + "\n" + 'crit_chance ' + str(w['crit_chance']) + "\n" + 'crit_multip ' + str(
        w['crit_multip']) + "\n" + 'fire_rate ' + str(w['fire_rate']) + "\n" + 'magazine ' + str(
        w['magazine']) + "\n" + 'reload ' + str(w['reload']) + "\n" + 'status ' + str(
        w['status']) + "\n" + 'impact ' + str(w['impact']) + "\n" + 'slash ' + str(w['slash']) + "\n" + \
        'puncture ' + str(w['puncture']) + "\n" + 'elem ' + str(w['elem']) + '\n\n' + \
        'w_dmg_buff ' + str(w['w_dmg_buff'])

    w_stats_window.delete(0.0, END)
    w_stats_window.insert(END, s)
    calculator()


clr_bgr = '#2b2b2b'
clr_fgr = '#a9b7c6'  # '#bbbbbb' #a9b7c6 '#cfcfcf'
clr_frm_header = '#ccff00'
clr_d_bgr = '#3b3b3b'
clr_d_fgr = '#cfcfcf'  # '#818181'
clr_btn_bgr = '#365880'  # 'gray'
clr_btn_fgr = 'white'

window = Tk()
window.title("Warframe calc")
# window.geometry('350x200')
# window.configure(background='#2b2b2b')
# window.geometry('620x620')
window.tk_setPalette(background=clr_bgr, foreground=clr_fgr, activeBackground=clr_bgr, activeForeground=clr_fgr)

# Frame Weapons -----------------------------------------------------------------------------------------------
spec_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
spec_frame.grid(row=0, column=0, sticky=(N, W, E, S))

n_row = 0
Label(spec_frame, text="Weapon:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)

weapons = load_pickle('wf_weapons')
w_list = []
for weapon in weapons:
    w_list.append(weapon)

cbx_selected_weapon = ttk.Combobox(spec_frame)
cbx_selected_weapon.bind("<<ComboboxSelected>>", pick_weapon)
cbx_selected_weapon['values'] = w_list
cbx_selected_weapon.current(0)  # set the selected item
cbx_selected_weapon.grid(column=1, row=n_row)

n_row += 1
w_stats_window = Text(spec_frame, width=20, height=17, wrap="word", font=("Courier New", 9))
w_stats_window.grid(row=n_row, column=0, columnspan=1, sticky=W)

w_multipl_window = Text(spec_frame, width=20, height=17, wrap="word", font=("Courier New", 9))
w_multipl_window.grid(row=n_row, column=1, columnspan=1, sticky=W)

w_full_window = Text(spec_frame, width=20, height=17, wrap="word", font=("Courier New", 9))
w_full_window.grid(row=n_row, column=2, columnspan=1, sticky=W)


# Frame Mods -----------------------------------------------------------------------------------------------
# Shotgun Mods -----------------------------------------------------------------------------------------------
shotgun_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
shotgun_frame.grid(row=0, column=1, rowspan=1, sticky=(N, W, E, S))
if True:
    n_row = 0
    Label(shotgun_frame, text="Shotgun", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    p_point_blank = IntVar()
    Checkbutton(shotgun_frame, text="Primed Point Blank(Shotgun)", selectcolor=clr_bgr, command=apply_mods,
                variable=p_point_blank).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    hells_chamber = IntVar()
    Checkbutton(shotgun_frame, text="Hells Chamber(Shotgun)", selectcolor=clr_bgr, command=apply_mods,
                variable=hells_chamber).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    blaze = IntVar()
    Checkbutton(shotgun_frame, text="Blaze(Shotgun)", selectcolor=clr_bgr, command=apply_mods, variable=blaze).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    p_charged_shell = IntVar()
    Checkbutton(shotgun_frame, text="Primed Charged Shell(Shotgun)", selectcolor=clr_bgr, command=apply_mods,
                variable=p_charged_shell).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    chilling_reload = IntVar()
    Checkbutton(shotgun_frame, text="Chilling Reload(Shotgun)", selectcolor=clr_bgr, command=apply_mods,
                variable=chilling_reload).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    ammo_stock = IntVar()
    Checkbutton(shotgun_frame, text="Ammo Stock(Shotgun)", selectcolor=clr_bgr, command=apply_mods,
                variable=ammo_stock).grid(row=n_row, column=0, sticky=W)

# Rifle Mods -----------------------------------------------------------------------------------------------
rifle_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
rifle_frame.grid(row=0, column=2, rowspan=1, sticky=(N, W, E, S))
if True:
    n_row = 0
    Label(rifle_frame, text="Rifle", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    serration = IntVar()
    Checkbutton(rifle_frame, text="Serration (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=serration).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    split_chamber = IntVar()
    Checkbutton(rifle_frame, text="Split Chamber (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=split_chamber).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    point_strike = IntVar()
    Checkbutton(rifle_frame, text="Point Strike (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=point_strike).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    vital_sense = IntVar()
    Checkbutton(rifle_frame, text="Vital Sense (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=vital_sense).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    heavy_caliber = IntVar()
    Checkbutton(rifle_frame, text="Heavy Caliber (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=heavy_caliber).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    p_cryo_rounds = IntVar()
    Checkbutton(rifle_frame, text="Primed Cryo Rounds (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=p_cryo_rounds).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    crash_course = IntVar()
    Checkbutton(rifle_frame, text="Crash Course (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=crash_course).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    critical_dealy = IntVar()
    Checkbutton(rifle_frame, text="Critical Dealy (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=critical_dealy).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    hammer_shot = IntVar()
    Checkbutton(rifle_frame, text="Hammer Shot (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=hammer_shot).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    wildfire = IntVar()
    Checkbutton(rifle_frame, text="Wildfire (Rifle)", selectcolor=clr_bgr, command=apply_mods, variable=wildfire).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    speed_trigger = IntVar()
    Checkbutton(rifle_frame, text="Speed Trigger (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=speed_trigger).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    vile_acceleration = IntVar()
    Checkbutton(rifle_frame, text="Vile Acceleration (Rifle)", selectcolor=clr_bgr, command=apply_mods,
                variable=vile_acceleration).grid(row=n_row, column=0, sticky=W)

# Mixed Mods -----------------------------------------------------------------------------------------------
mixed_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
mixed_frame.grid(row=1, column=1, rowspan=1, sticky=(N, W, E, S))
if True:
    n_row = 0
    electric6060 = IntVar()
    Checkbutton(mixed_frame, text="Electricity 60 60", selectcolor=clr_bgr, command=apply_mods,
                variable=electric6060).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    toxin6060 = IntVar()
    Checkbutton(mixed_frame, text="Toxin 60 60", selectcolor=clr_bgr, command=apply_mods, variable=toxin6060).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    cold6060 = IntVar()
    Checkbutton(mixed_frame, text="Cold 60 60", selectcolor=clr_bgr, command=apply_mods, variable=cold6060).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    heat6060 = IntVar()
    Checkbutton(mixed_frame, text="Heat 60 60", selectcolor=clr_bgr, command=apply_mods, variable=heat6060).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    electric90 = IntVar()
    Checkbutton(mixed_frame, text="Electricity 90", selectcolor=clr_bgr, command=apply_mods, variable=electric90).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    toxin90 = IntVar()
    Checkbutton(mixed_frame, text="Toxin 90", selectcolor=clr_bgr, command=apply_mods, variable=toxin90).grid(row=n_row,
                                                                                                              column=0,
                                                                                                              sticky=W)
    n_row += 1
    cold90 = IntVar()
    Checkbutton(mixed_frame, text="Cold 90", selectcolor=clr_bgr, command=apply_mods, variable=cold90).grid(row=n_row,
                                                                                                            column=0,
                                                                                                            sticky=W)
    n_row += 1
    heat90 = IntVar()
    Checkbutton(mixed_frame, text="Heat 90", selectcolor=clr_bgr, command=apply_mods, variable=heat90).grid(row=n_row,
                                                                                                            column=0,
                                                                                                            sticky=W)
    n_row += 1
    vigilante_armaments = IntVar()
    Checkbutton(mixed_frame, text="Vigilante Armaments (Primary)", selectcolor=clr_bgr, command=apply_mods,
                variable=vigilante_armaments).grid(row=n_row, column=0, sticky=W)

# Melee Mods -----------------------------------------------------------------------------------------------
melee_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
melee_frame.grid(row=1, column=2, rowspan=1, sticky=(N, W, E, S))
if True:
    n_row = 0
    Label(melee_frame, text="Melee", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    p_fevr_strike = IntVar()
    Checkbutton(melee_frame, text="Primed Fever Strike", selectcolor=clr_bgr, command=apply_mods,
                variable=p_fevr_strike).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    sacrf_steel = IntVar()
    Checkbutton(melee_frame, text="Sacrifical Steel", selectcolor=clr_bgr, command=apply_mods,
                variable=sacrf_steel).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    p_pressure_point = IntVar()
    Checkbutton(melee_frame, text="Primed Pressure Point", selectcolor=clr_bgr, command=apply_mods,
                variable=p_pressure_point).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    spoiled_strike = IntVar()
    Checkbutton(melee_frame, text="Spoiled Strike", selectcolor=clr_bgr, command=apply_mods,
                variable=spoiled_strike).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    organ_shatter = IntVar()
    Checkbutton(melee_frame, text="Organ Shatter", selectcolor=clr_bgr, command=apply_mods,
                variable=organ_shatter).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    true_steel = IntVar()
    Checkbutton(melee_frame, text="True Steel", selectcolor=clr_bgr, command=apply_mods,
                variable=true_steel).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    gladiator_might = IntVar()
    Checkbutton(melee_frame, text="Gladiator Might", selectcolor=clr_bgr, command=apply_mods,
                variable=gladiator_might).grid(row=n_row, column=0, sticky=W)

# Frame Riven 1-----------------------------------------------------------------------------------------------
riven_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
riven_frame.grid(row=0, column=3, rowspan=2, sticky=(N, W, E, S))
if True:
    r_crit_chance = DoubleVar()
    r_crit_chance.set(0)
    r_crit_dmg = DoubleVar()
    r_crit_dmg.set(0)
    r_heat = DoubleVar()
    r_heat.set(0)
    r_electricity = DoubleVar()
    r_electricity.set(0)
    r_cold = DoubleVar()
    r_cold.set(0)
    r_toxin = DoubleVar()
    r_toxin.set(0)
    r_multishot = DoubleVar()
    r_multishot.set(0)
    r_damage = DoubleVar()
    r_damage.set(0)
    r_status = DoubleVar()
    r_status.set(0)
    r_slash = DoubleVar()
    r_slash.set(0)
    r_impact = DoubleVar()
    r_impact.set(0)
    r_puncture = DoubleVar()
    r_puncture.set(0)
    r_reload = DoubleVar()
    r_reload.set(0)
    r_magazine = DoubleVar()
    r_magazine.set(0)
    r_fire_rate = DoubleVar()
    r_fire_rate.set(0)

    n_row = 0
    apply_riven1 = IntVar()
    apply_riven2 = IntVar()
    Checkbutton(riven_frame, text="Apply Riven 1", selectcolor=clr_bgr, command=apply_mods, variable=apply_riven1).grid(
        row=n_row, column=0, sticky=W)
    n_row += 1
    Label(riven_frame, text="Damage:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_damage, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame, text="Multishot:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_multishot, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Crit Chance:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_crit_chance, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Crit Dmg:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_crit_dmg, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Heat:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_heat, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                           column=1)
    n_row += 1
    Label(riven_frame, text="Electricity:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_electricity, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Toxin:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_cold, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                           column=1)
    n_row += 1
    Label(riven_frame, text="Cold:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_toxin, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                            column=1)
    n_row += 1
    Label(riven_frame, text="Status:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_status, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame, text="Slash:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_slash, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                            column=1)
    n_row += 1
    Label(riven_frame, text="Impact:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_impact, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame, text="Puncture:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_puncture, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Reload:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_reload, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame, text="Magazine:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_magazine, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame, text="Fire Rate:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=r_fire_rate, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    chroma_buff = DoubleVar()
    chroma_buff.set(0)
    Label(riven_frame, text="Chroma buff 6.51:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame, width=7, textvariable=chroma_buff, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Text(riven_frame, height=8, width=20, wrap="word", font=("Courier New", 9)).grid(row=n_row, column=0, columnspan=2, sticky=(W, E))

# Frame Riven 2-----------------------------------------------------------------------------------------------
riven_frame2 = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
riven_frame2.grid(row=0, column=4, rowspan=2, sticky=(N, W, E, S))
if True:
    r2_crit_chance = DoubleVar()
    r2_crit_chance.set(0)
    r2_crit_dmg = DoubleVar()
    r2_crit_dmg.set(0)
    r2_heat = DoubleVar()
    r2_heat.set(0)
    r2_electricity = DoubleVar()
    r2_electricity.set(0)
    r2_cold = DoubleVar()
    r2_cold.set(0)
    r2_toxin = DoubleVar()
    r2_toxin.set(0)
    r2_multishot = DoubleVar()
    r2_multishot.set(0)
    r2_damage = DoubleVar()
    r2_damage.set(0)
    r2_status = DoubleVar()
    r2_status.set(0)
    r2_slash = DoubleVar()
    r2_slash.set(0)
    r2_impact = DoubleVar()
    r2_impact.set(0)
    r2_puncture = DoubleVar()
    r2_puncture.set(0)
    r2_reload = DoubleVar()
    r2_reload.set(0)
    r2_magazine = DoubleVar()
    r2_magazine.set(0)
    r2_fire_rate = DoubleVar()
    r2_fire_rate.set(0)

    n_row = 0
    Checkbutton(riven_frame2, text="Apply Riven 2", selectcolor=clr_bgr, command=apply_mods,
                variable=apply_riven2).grid(row=n_row, column=0, sticky=W)
    n_row += 1
    Label(riven_frame2, text="Damage:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_damage, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Multishot:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_multishot, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Crit Chance:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_crit_chance, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Crit Dmg:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_crit_dmg, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Heat:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_heat, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame2, text="Electricity:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_electricity, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Toxin:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_cold, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                             column=1)
    n_row += 1
    Label(riven_frame2, text="Cold:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_toxin, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                              column=1)
    n_row += 1
    Label(riven_frame2, text="Status:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_status, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Slash:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_slash, validate="focusout", validatecommand=apply_mods).grid(row=n_row,
                                                                                                              column=1)
    n_row += 1
    Label(riven_frame2, text="Impact:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_impact, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Puncture:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_puncture, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Reload:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_reload, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Magazine:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_magazine, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Label(riven_frame2, text="Fire Rate:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=r2_fire_rate, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    chroma_buff2 = DoubleVar()
    chroma_buff2.set(0)
    Label(riven_frame2, text="Chroma buff 6.51:", foreground=clr_frm_header).grid(row=n_row, column=0, sticky=W)
    Entry(riven_frame2, width=7, textvariable=chroma_buff2, validate="focusout", validatecommand=apply_mods).grid(
        row=n_row, column=1)
    n_row += 1
    Text(riven_frame2, height=8, width=20, wrap="word", font=("Courier New", 9)).grid(row=n_row, column=0, columnspan=2, sticky=(W, E))

# ---------------------- Notes Frame
notes_frame = Frame(window, bd=2, relief=GROOVE)  # text="Options: ", padding="9 9 12 12"
notes_frame.grid(row=1, column=0, sticky=(N, W, E, S))

n_row = 0
note = """Rubico riv: 1.152 dmg, 1.041 crit, 0.652 elec, -0.659 impact

Rubico scoped  x1.5 total dmg + 0.35/0.50 crit_dmg multiplier

Vectis riv: 1.524 Crit chance + 0.956 Heat -0.226 Reload
Similuacrum stats are different, + aplies dmg buff(debuff) on dmg mods"""
# Label(notes_frame, text=note, foreground=clr_frm_header).grid(row=n_row, column=0, sticky=(W, N))
text_note = Text(notes_frame, height=12, width=61, wrap="word", font=("Courier New", 9))
text_note.grid(row=n_row, column=0, columnspan=2, sticky=(W, E))
# text_note.delete(0.0, END)
text_note.insert(END, note)

window.mainloop()
