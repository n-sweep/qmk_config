#!/usr/bin/env python3
# Clean up a keymap json

import json

key_data = {
    'KC_A': {'desc': 'A', 'aliases': []},
    'KC_B': {'desc': 'B', 'aliases': []},
    'KC_C': {'desc': 'C', 'aliases': []},
    'KC_D': {'desc': 'D', 'aliases': []},
    'KC_E': {'desc': 'E', 'aliases': []},
    'KC_F': {'desc': 'F', 'aliases': []},
    'KC_G': {'desc': 'G', 'aliases': []},
    'KC_H': {'desc': 'H', 'aliases': []},
    'KC_I': {'desc': 'I', 'aliases': []},
    'KC_J': {'desc': 'J', 'aliases': []},
    'KC_K': {'desc': 'K', 'aliases': []},
    'KC_L': {'desc': 'L', 'aliases': []},
    'KC_M': {'desc': 'M', 'aliases': []},
    'KC_N': {'desc': 'N', 'aliases': []},
    'KC_O': {'desc': 'O', 'aliases': []},
    'KC_P': {'desc': 'P', 'aliases': []},
    'KC_Q': {'desc': 'Q', 'aliases': []},
    'KC_R': {'desc': 'R', 'aliases': []},
    'KC_S': {'desc': 'S', 'aliases': []},
    'KC_T': {'desc': 'T', 'aliases': []},
    'KC_U': {'desc': 'U', 'aliases': []},
    'KC_V': {'desc': 'V', 'aliases': []},
    'KC_W': {'desc': 'W', 'aliases': []},
    'KC_X': {'desc': 'X', 'aliases': []},
    'KC_Y': {'desc': 'Y', 'aliases': []},
    'KC_Z': {'desc': 'Z', 'aliases': []},
    'KC_1': {'desc': '1', 'aliases': []},
    'KC_2': {'desc': '2', 'aliases': []},
    'KC_3': {'desc': '3', 'aliases': []},
    'KC_4': {'desc': '4', 'aliases': []},
    'KC_5': {'desc': '5', 'aliases': []},
    'KC_6': {'desc': '6', 'aliases': []},
    'KC_7': {'desc': '7', 'aliases': []},
    'KC_8': {'desc': '8', 'aliases': []},
    'KC_9': {'desc': '9', 'aliases': []},
    'KC_0': {'desc': '0', 'aliases': []},
    'KC_F1': {'desc': 'F1', 'aliases': []},
    'KC_F2': {'desc': 'F2', 'aliases': []},
    'KC_F3': {'desc': 'F3', 'aliases': []},
    'KC_F4': {'desc': 'F4', 'aliases': []},
    'KC_F5': {'desc': 'F5', 'aliases': []},
    'KC_F6': {'desc': 'F6', 'aliases': []},
    'KC_F7': {'desc': 'F7', 'aliases': []},
    'KC_F8': {'desc': 'F8', 'aliases': []},
    'KC_F9': {'desc': 'F9', 'aliases': []},
    'KC_F10': {'desc': 'F10', 'aliases': []},
    'KC_F11': {'desc': 'F11', 'aliases': []},
    'KC_F12': {'desc': 'F12', 'aliases': []},
    'KC_F13': {'desc': 'F13', 'aliases': []},
    'KC_F14': {'desc': 'F14', 'aliases': []},
    'KC_F15': {'desc': 'F15', 'aliases': []},
    'KC_F16': {'desc': 'F16', 'aliases': []},
    'KC_F17': {'desc': 'F17', 'aliases': []},
    'KC_F18': {'desc': 'F18', 'aliases': []},
    'KC_F19': {'desc': 'F19', 'aliases': []},
    'KC_F20': {'desc': 'F20', 'aliases': []},
    'KC_F21': {'desc': 'F21', 'aliases': []},
    'KC_F22': {'desc': 'F22', 'aliases': []},
    'KC_F23': {'desc': 'F23', 'aliases': []},
    'KC_F24': {'desc': 'F24', 'aliases': []},
    'KC_ENTER': {'desc': 'Enter', 'aliases': ['KC_ENT']},
    'KC_ESCAPE': {'desc': 'Esc', 'aliases': ['KC_ESC']},
    'KC_BACKSPACE': {'desc': 'Del', 'aliases': ['KC_BSPC']},
    'KC_TAB': {'desc': 'Tab', 'aliases': []},
    'KC_SPACE': {'desc': 'Space', 'aliases': ['KC_SPC']},
    'KC_MINUS': {'desc': '-', 'aliases': ['KC_MINS']},
    'KC_EQUAL': {'desc': '=', 'aliases': ['KC_EQL']},
    'KC_LEFT_BRACKET': {'desc': '[', 'aliases': ['KC_LBRC']},
    'KC_RIGHT_BRACKET': {'desc': ']', 'aliases': ['KC_RBRC']},
    'KC_BACKSLASH': {'desc': '\\', 'aliases': ['KC_BSLS']},
    'KC_SEMICOLON': {'desc': ';', ['KC_SCLN']},
    'KC_QUOTE': {'desc': "'", 'aliases': ['KC_QUOT']},
    'KC_GRAVE': {'desc': '`', 'aliases': ['KC_GRV']},
    'KC_COMMA': {'desc': ',', 'aliases': ['KC_COMM']},
    'KC_DOT': {'desc': '.', 'aliases': []},
    'KC_SLASH': {'desc': '/', 'aliases': ['KC_SLSH']},
    'KC_CAPS_LOCK': {'desc': 'Caps', 'aliases': ['KC_CAPS']},
    'KC_LOCKING_CAPS_LOCK': {'desc': 'CapsLk', 'aliases': ['KC_LCAP']},
    'KC_LOCKING_NUM_LOCK': {'desc': 'NumLk', 'aliases': ['KC_LNUM']},
    'KC_LOCKING_SCROLL_LOCK': {'desc': 'ScrlLk', 'aliases': ['KC_LSCR']},

}


def main():
    fp = './nyquist_final_0.json'
    n_rows = 5
    n_cols = 12

    with open(fp, 'r') as f:
        data = json.load(f)

    for layer in data['layers']:
        keys = []
        widths = [0 for _ in range(n_cols)]
        w = 0

        for r in range(n_rows):
            a = r * n_cols
            b = a + n_cols
            slc = layer[a:b]

            for i, key in enumerate(slc):
                widths[i] = max(len(key), widths[i])
                w = max(len(key), w)

            keys.append(slc)

        for row in keys:
            row_str = [f'{key},'.ljust(widths[i] + 1) for i, key in enumerate(row)]
            print(' '.join(row_str))

        print('\n')


if __name__ == "__main__":
    main()
