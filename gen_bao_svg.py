# -*- coding: utf-8 -*-
"""生成包覆式外帳步驟示意圖（暗色系 SVG），對應第 7–12 頁左側圖像。
依手繪圖紙（包覆式外帳1–3）的五固定點方法與講解文字重製。"""
from pathlib import Path
OUT = Path("images")

INK="#d9e2da"; MUTE="#93a0a8"; TARP="#5C7F52"; TARP2="#7FA06B"
ORANGE="#e8643a"; CYAN="#4fc3f7"; ROPE="#ffb74d"; RED="#ff7a6b"
GREEN="#81c784"; TEXT="#e9f0ea"; POLE="#c3cad2"; GROUND="#6b5535"
FF = '"Microsoft JhengHei","Noto Sans TC",sans-serif'
VW, VH = 1000, 660

x0, y0, x1, y1 = 175, 150, 825, 520
qx = [x0, 337.5, 500, 662.5, x1]
qy = [y0, 242.5, 335, 427.5, y1]
P = {
    "E": (x0, y0), "D": (337.5, y0), "C": (500, y0), "B": (662.5, y0), "A": (x1, y0),
    "P": (x1, 242.5), "O": (x1, 335), "N": (x1, 427.5), "M": (x1, y1),
    "L": (662.5, y1), "K": (500, y1), "J": (337.5, y1), "I": (x0, y1),
    "H": (x0, 427.5), "G": (x0, 335), "F": (x0, 242.5),
}
CEN = (500, 335)
PT3 = (662.5, 427.5)
PT4 = (337.5, 427.5)


def svg(inner):
    return (f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{VW}\" height=\"{VH}\" "
            f"viewBox=\"0 0 {VW} {VH}\" font-family='{FF}'>" + inner + "</svg>")


def tarp(op=0.42):
    s = (f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="10" '
         f'fill="{TARP}" fill-opacity="{op}" stroke="{INK}" stroke-width="3.5"/>')
    for i in (1, 2, 3):
        s += f'<line x1="{qx[i]}" y1="{y0}" x2="{qx[i]}" y2="{y1}" stroke="{INK}" stroke-opacity="0.18" stroke-width="1.5"/>'
        s += f'<line x1="{x0}" y1="{qy[i]}" x2="{x1}" y2="{qy[i]}" stroke="{INK}" stroke-opacity="0.18" stroke-width="1.5"/>'
    return s


OFF = {"E": (-4, -16, "end"), "D": (0, -16, "middle"), "C": (0, -16, "middle"), "B": (0, -16, "middle"), "A": (4, -16, "start"),
       "P": (16, 6, "start"), "O": (16, 6, "start"), "N": (16, 6, "start"), "M": (14, 24, "start"),
       "L": (0, 30, "middle"), "K": (0, 30, "middle"), "J": (0, 30, "middle"), "I": (-4, 26, "end"),
       "H": (-16, 6, "end"), "G": (-16, 6, "end"), "F": (-16, 6, "end")}


def labels():
    s = ""
    for k in "ABCDEFGHIJKLMNOP":
        x, y = P[k]; dx, dy, anc = OFF[k]
        s += f'<circle cx="{x}" cy="{y}" r="4.5" fill="{INK}" fill-opacity="0.75"/>'
        s += f'<text x="{x+dx}" y="{y+dy}" font-size="22" fill="{MUTE}" text-anchor="{anc}">{k}</text>'
    return s


def badge(x, y, n, fill=ORANGE, r=25):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#0d1117" stroke-width="2"/>'
            f'<text x="{x}" y="{y+9}" font-size="26" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')


def stake(x, y):
    return (f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+22}" stroke="{POLE}" stroke-width="5"/>'
            f'<path d="M{x-9},{y+22} L{x+9},{y+22} L{x},{y+38} Z" fill="{POLE}"/>')


def cap(text, color=TEXT, y=628, x=VW / 2, size=25):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="700" fill="{color}" text-anchor="middle">{text}</text>'


def defs():
    return ('<defs>'
            f'<marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto"><path d="M0,0 L9,5 L0,10 z" fill="{RED}"/></marker>'
            f'<marker id="ao" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto"><path d="M0,0 L9,5 L0,10 z" fill="{ROPE}"/></marker>'
            '</defs>')


# bao_0
s = defs() + tarp() + labels()
s += badge(*P["B"], "1") + badge(*P["D"], "2") + badge(*PT3, "3") + badge(*PT4, "4") + badge(*CEN, "5", CYAN, 27)
my = PT3[1] + 52
s += f'<line x1="{PT4[0]}" y1="{my}" x2="{PT3[0]}" y2="{my}" stroke="{RED}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>'
s += f'<text x="{CEN[0]}" y="{my+26}" font-size="24" font-weight="700" fill="{RED}" text-anchor="middle">第3 ↔ 第4：約 160–165 cm</text>'
s += f'<text x="{CEN[0]}" y="{CEN[1]-38}" font-size="22" font-weight="700" fill="{CYAN}" text-anchor="middle">登山杖 120–125 cm</text>'
s += cap("五固定點：B①、D② 上緣　N③、H④ 往內　中央登山杖⑤", GREEN)
(OUT / "bao_0.svg").write_text(svg(s), encoding="utf-8")

# bao_1
s = defs() + tarp() + labels()
for k, n in (("B", "1"), ("D", "2")):
    x, y = P[k]
    s += f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="{INK}" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="8 7"/>'
    s += stake(x, y0 - 2)
s += f'<text x="{(x0+P["D"][0])/2}" y="{y1+34}" font-size="22" fill="{MUTE}" text-anchor="middle">← ¼ →</text>'
s += f'<text x="{(P["B"][0]+x1)/2}" y="{y1+34}" font-size="22" fill="{MUTE}" text-anchor="middle">← ¼ →</text>'
s += badge(P["B"][0], y0 - 30, "1") + badge(P["D"][0], y0 - 30, "2")
s += cap("B 為第1固定點、D 為第2固定點：上緣左右各約四分之一處先下釘", GREEN)
(OUT / "bao_1.svg").write_text(svg(s), encoding="utf-8")

# bao_2
s = defs() + tarp() + labels()
band_y = P["N"][1]
s += f'<rect x="{x0}" y="{band_y}" width="{x1-x0}" height="{y1-band_y}" fill="{RED}" fill-opacity="0.20"/>'
s += f'<line x1="{x0}" y1="{band_y}" x2="{x1}" y2="{band_y}" stroke="{RED}" stroke-width="3" stroke-dasharray="12 8"/>'
for bx in (337.5, 500, 662.5):
    s += f'<line x1="{bx}" y1="{band_y+10}" x2="{bx}" y2="{y1-14}" stroke="{RED}" stroke-width="3.5" marker-end="url(#ar)"/>'
s += badge(*P["N"], "3", ORANGE, 22) + badge(*P["H"], "4", ORANGE, 22)
s += cap("將 N、H 掛點以下約四分之一的布往下折，整理後暫時固定", RED)
(OUT / "bao_2.svg").write_text(svg(s), encoding="utf-8")

# bao_3
s = defs() + tarp() + labels()
s += f'<line x1="{P["N"][0]-8}" y1="{P["N"][1]}" x2="{PT3[0]+10}" y2="{PT3[1]}" stroke="{RED}" stroke-width="4" marker-end="url(#ar)"/>'
s += f'<line x1="{P["H"][0]+8}" y1="{P["H"][1]}" x2="{PT4[0]-10}" y2="{PT4[1]}" stroke="{RED}" stroke-width="4" marker-end="url(#ar)"/>'
s += stake(*PT3) + stake(*PT4) + badge(*PT3, "3") + badge(*PT4, "4")
ry = 250
s += f'<line x1="{PT4[0]}" y1="{ry}" x2="{PT3[0]}" y2="{ry}" stroke="{ROPE}" stroke-width="6"/>'
s += f'<circle cx="{PT4[0]}" cy="{ry}" r="10" fill="{ROPE}"/><circle cx="{PT3[0]}" cy="{ry}" r="10" fill="{ROPE}"/>'
s += f'<text x="{CEN[0]}" y="{ry-16}" font-size="22" font-weight="700" fill="{ROPE}" text-anchor="middle">兩頭打結營繩 160–165 cm</text>'
s += f'<line x1="{PT4[0]}" y1="{PT4[1]+40}" x2="{PT3[0]}" y2="{PT3[1]+40}" stroke="{RED}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>'
s += f'<text x="{CEN[0]}" y="{PT3[1]+64}" font-size="23" font-weight="700" fill="{RED}" text-anchor="middle">第3 ↔ 第4：160–165 cm</text>'
s += cap("營繩拉直平鋪地面，量出並下釘固定第3(N)、第4(H)點", RED)
(OUT / "bao_3.svg").write_text(svg(s), encoding="utf-8")

# bao_4 (side view)
gy = 520
s = defs()
s += f'<rect x="0" y="{gy}" width="{VW}" height="{VH-gy}" fill="{GROUND}" fill-opacity="0.35"/>'
s += f'<line x1="0" y1="{gy}" x2="{VW}" y2="{gy}" stroke="{GROUND}" stroke-width="4"/>'
apex = (500, 175); back = (815, gy - 4); front = (185, gy - 4)   # 對稱置中於 x=500
s += f'<path d="M{apex[0]} {apex[1]} L{back[0]} {back[1]} L{apex[0]} {gy-4} Z" fill="{TARP}" fill-opacity="0.8" stroke="{INK}" stroke-width="3"/>'
s += f'<path d="M{apex[0]} {apex[1]} L{front[0]} {front[1]} L{apex[0]} {gy-4} Z" fill="{TARP2}" fill-opacity="0.55" stroke="{INK}" stroke-width="2.5"/>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]}" y2="{gy-4}" stroke="{POLE}" stroke-width="9"/>'
s += f'<circle cx="{apex[0]}" cy="{apex[1]}" r="9" fill="{ROPE}"/>'
s += f'<text x="{apex[0]}" y="{apex[1]-14}" font-size="20" font-weight="700" fill="{ROPE}" text-anchor="middle">上方用繩綁緊</text>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="120" y2="{gy-4}" stroke="{ROPE}" stroke-width="4" stroke-dasharray="12 8"/>'
s += stake(120, gy - 4) + stake(back[0], gy - 4) + stake(front[0], gy - 4)
s += badge(apex[0], apex[1] - 58, "5", CYAN, 25)
s += f'<text x="{apex[0]-8}" y="{gy-120}" font-size="22" font-weight="700" fill="{CYAN}" text-anchor="middle">登山杖 120–125 cm</text>'
s += cap("穿入天幕下方垂直撐起 → 上方綁緊 → 往外拉繩下釘固定", GREEN)
(OUT / "bao_4.svg").write_text(svg(s), encoding="utf-8")

# bao_done (side view + vestibule)
gy = 520
s = defs()
s += f'<rect x="0" y="{gy}" width="{VW}" height="{VH-gy}" fill="{GROUND}" fill-opacity="0.35"/>'
s += f'<line x1="0" y1="{gy}" x2="{VW}" y2="{gy}" stroke="{GROUND}" stroke-width="4"/>'
apex = (500, 165); back = (815, gy - 4); front = (185, gy - 4)   # 對稱置中於 x=500
s += f'<path d="M{apex[0]} {apex[1]} L{back[0]} {back[1]} L{apex[0]} {gy-4} Z" fill="{TARP}" fill-opacity="0.85" stroke="{INK}" stroke-width="3"/>'
s += f'<path d="M{apex[0]} {apex[1]} L{front[0]} {front[1]} L{apex[0]} {gy-4} Z" fill="{TARP2}" fill-opacity="0.5" stroke="{INK}" stroke-width="2.5"/>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]}" y2="{gy-4}" stroke="{POLE}" stroke-width="9"/>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="120" y2="{gy-4}" stroke="{ROPE}" stroke-width="4" stroke-dasharray="12 8"/>'
s += stake(120, gy - 4) + stake(back[0], gy - 4) + stake(front[0], gy - 4)
s += f'<text x="650" y="395" font-size="23" font-weight="700" fill="#fff" text-anchor="middle">封閉式帳身</text>'
s += f'<text x="330" y="{gy-30}" font-size="21" font-weight="700" fill="{TEXT}" text-anchor="middle">前庭（可炊煮）</text>'
s += f'<line x1="255" y1="{gy-70}" x2="305" y2="{gy-20}" stroke="{RED}" stroke-width="3.5" marker-end="url(#ar)"/>'
s += f'<line x1="760" y1="{gy-70}" x2="715" y2="{gy-20}" stroke="{RED}" stroke-width="3.5" marker-end="url(#ar)"/>'
s += f'<text x="{VW/2}" y="120" font-size="22" font-weight="700" fill="{GREEN}" text-anchor="middle">多餘布料「由外往內」塞並封起</text>'
s += cap("用登山杖的繩把布面往外拉起，增加帳內頭部高度與空間", GREEN)
(OUT / "bao_done.svg").write_text(svg(s), encoding="utf-8")

print("Generated:", *[p.name for p in sorted(OUT.glob("bao_*.svg"))])
