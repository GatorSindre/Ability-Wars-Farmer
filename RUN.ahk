#Requires AutoHotkey v2.0

; Coordinates
gator_yield := [484, 111]
gator_focus := [484, 111 - 60]
gator_e := [92, 452]

potato_yield := [487, 627]
potato_focus := [487, 627 - 60]

alt1_yield := [1446, 113]
alt1_focus := [1446, 113 - 60]

on_screen_enter := [1650, 832]

; Timings (in seconds)
focus_cooldown := 1
yield_cooldown := 0.4
tween_cooldown := 2
enter_cooldown := 0.2
key_cooldown := 0.4

alt1Navn := "tomtatohandye"

; ==============================
; Functions
; ==============================

armySpawn() {
    global gator_yield, gator_focus, gator_e, on_screen_enter
    global focus_cooldown, yield_cooldown, tween_cooldown, enter_cooldown, key_cooldown

    MouseClick("left", gator_focus[1], gator_focus[2])
    Sleep(focus_cooldown * 1000)

    MouseClick("left", gator_yield[1], gator_yield[2])
    Sleep(yield_cooldown * 1000)

    Send("twp army")
    Sleep(yield_cooldown * 1000)

    Send("{Enter}")
    Sleep(key_cooldown * 1000)

    Sleep(tween_cooldown * 1000)

    MouseClick("left", gator_e[1], gator_e[2])
    Sleep(500)

    MouseClick("left", gator_yield[1], gator_yield[2])
    Sleep(yield_cooldown * 1000)

    Send("twp default")
    Sleep(yield_cooldown * 1000)

    Send("{Enter}")
    Sleep(key_cooldown * 1000)

    Sleep(tween_cooldown * 1000)
}

punch() {
    global gator_focus, gator_yield, alt1_focus, alt1_yield, on_screen_enter, alt1Navn
    global focus_cooldown, yield_cooldown, tween_cooldown, enter_cooldown

    ; alt1 punch sequence
    MouseClick("left", alt1_focus[1], alt1_focus[2])
    Sleep(focus_cooldown * 1000)

    MouseClick("left", alt1_yield[1], alt1_yield[2])
    Sleep(yield_cooldown * 1000)

    Send("twp look_set")
    Sleep(yield_cooldown * 1000)

    Send("{Enter}")
    Sleep(enter_cooldown * 1000)

    Sleep(tween_cooldown * 1000)

    ; gator look at alt1
    MouseClick("left", gator_focus[1], gator_focus[2])
    Sleep(focus_cooldown * 1000)

    MouseClick("left", gator_yield[1], gator_yield[2])
    Sleep(yield_cooldown * 1000)

    Send("lookat " alt1Navn)
    Sleep(yield_cooldown * 1000)

    Send("{Enter}")
    Sleep(enter_cooldown * 1000)

    Sleep(focus_cooldown * 1000)

    Send("o") ; optional key press
    Sleep(focus_cooldown * 1000)

    ; alt1 get punched
    MouseClick("left", alt1_focus[1], alt1_focus[2])
    Sleep(focus_cooldown * 1000)

    MouseClick("left", alt1_yield[1], alt1_yield[2])
    Sleep(yield_cooldown * 1000)

    Send("twp get_punched")
    Sleep(yield_cooldown * 1000)

    Send("{Enter}")
    Sleep(enter_cooldown * 1000)

    Sleep(tween_cooldown * 1000)

    ; gator punch
    MouseClick("left", gator_focus[1], gator_focus[2])
    Sleep(focus_cooldown * 1000)

    MouseClick("left", gator_focus[1], gator_focus[2])
    Sleep(1000)
}

setup() {
    armySpawn()
    punch()
}

; ==============================
; Hotkeys
; ==============================

o::ExitApp  ; Exit script
u::setup() ; Run full setup