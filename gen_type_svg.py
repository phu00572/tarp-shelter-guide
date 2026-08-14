# -*- coding: utf-8 -*-
"""生成 A字帳 / 斜邊帳 / L型帳 的暗色系側視示意圖（SVG），對應第 14/16/17 頁左側圖。
風格與包覆式步驟圖（bao_*.svg）一致。"""
from pathlib import Path
OUT = Path("images")

INK="#d9e2da"; MUTE="#93a0a8"; TARP="#5C7F52"; TARP2="#7FA06B"; WALL="#3f5c39"
ORANGE="#e8643a"; CYAN="#4fc3f7"; ROPE="#ffb74d"; RED="#ff7a6b"
GREEN="#81c784"; TEXT="#e9f0ea"; POLE="#c3cad2"; GROUND="#6b5535"
FF = '"Microsoft JhengHei","Noto Sans TC",sans-serif'
VW, VH = 1000, 660
GY = 520


def svg(inner):
    return (f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{VW}\" height=\"{VH}\" "
            f"viewBox=\"0 0 {VW} {VH}\" font-family='{FF}'>" + inner + "</svg>")


def defs():
    return ('<defs>'
            f'<marker id="ao" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto"><path d="M0,0 L9,5 L0,10 z" fill="{ROPE}"/></marker>'
            '</defs>')


def ground():
    return (f'<rect x="0" y="{GY}" width="{VW}" height="{VH-GY}" fill="{GROUND}" fill-opacity="0.35"/>'
            f'<line x1="0" y1="{GY}" x2="{VW}" y2="{GY}" stroke="{GROUND}" stroke-width="4"/>')


def stake(x, y):
    return (f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+22}" stroke="{POLE}" stroke-width="5"/>'
            f'<path d="M{x-9},{y+22} L{x+9},{y+22} L{x},{y+38} Z" fill="{POLE}"/>')


def cap(text, color=GREEN, y=628, x=VW / 2, size=25):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="700" fill="{color}" text-anchor="middle">{text}</text>'


def txt(x, y, s, color=TEXT, size=22, anc="middle", bold=True):
    w = ' font-weight="700"' if bold else ''
    return f'<text x="{x}" y="{y}"{w} font-size="{size}" fill="{color}" text-anchor="{anc}">{s}</text>'


# ---------- A 字帳 ----------
s = defs() + ground()
apex = (500, 165); L = (235, GY - 4); R = (765, GY - 4)
s += f'<path d="M{L[0]} {L[1]} L{apex[0]} {apex[1]} L{R[0]} {R[1]} L{R[0]-34} {R[1]} L{apex[0]} {apex[1]+30} L{L[0]+34} {L[1]} Z" fill="{TARP}" fill-opacity="0.35"/>'
s += f'<path d="M{L[0]} {L[1]} L{apex[0]} {apex[1]} L{R[0]} {R[1]}" fill="none" stroke="{TARP}" stroke-width="20" stroke-linejoin="round"/>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]}" y2="{GY-4}" stroke="{POLE}" stroke-width="9"/>'
# guy lines ~45
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]-210}" y2="{GY-4}" stroke="{ROPE}" stroke-width="4.5" stroke-dasharray="14 9"/>'
s += f'<line x1="{apex[0]}" y1="{apex[1]}" x2="{apex[0]+210}" y2="{GY-4}" stroke="{ROPE}" stroke-width="4.5" stroke-dasharray="14 9"/>'
for sx in (L[0], R[0], apex[0] - 210, apex[0] + 210):
    s += stake(sx, GY - 4)
s += txt(apex[0], 120, '屋脊要「直挺」', GREEN, 26)
s += txt(apex[0] + 16, (apex[1] + GY) / 2, '主營柱／登山杖', POLE, 21, "start")
s += txt(apex[0] - 250, GY - 60, '營繩約 45°', ROPE, 20)
s += cap('中央撐高屋脊、拉出兩端屋簷、四角與側繩張緊')
(OUT / "a_frame_bare.svg").write_text(svg(s), encoding="utf-8")

# ---------- 斜邊帳（單斜面） ----------
s = defs() + ground()
high = (370, 165); edge = (790, GY - 4)
s += f'<path d="M{high[0]} {high[1]} L{edge[0]} {edge[1]} L{edge[0]-30} {edge[1]} L{high[0]} {high[1]+28} Z" fill="{TARP}" fill-opacity="0.35"/>'
s += f'<line x1="{high[0]}" y1="{high[1]}" x2="{edge[0]}" y2="{edge[1]}" stroke="{TARP}" stroke-width="20" stroke-linecap="round"/>'
s += f'<line x1="{high[0]}" y1="{high[1]}" x2="{high[0]}" y2="{GY-4}" stroke="{POLE}" stroke-width="9"/>'
s += f'<line x1="{high[0]}" y1="{high[1]}" x2="200" y2="{GY-4}" stroke="{ROPE}" stroke-width="4.5" stroke-dasharray="14 9"/>'
s += stake(200, GY - 4) + stake(high[0], GY - 4) + stake(edge[0], edge[1])
s += txt(high[0], 120, '一高一低．單斜面', GREEN, 26)
s += txt(high[0] - 16, (high[1] + GY) / 2, '高側營柱／登山杖', POLE, 20, "end")
s += txt(edge[0] - 60, GY + 40, '斜邊下緣下釘觸地', GREEN, 21, "middle")
s += cap('一側撐高、另一側斜拉下釘觸地；迎風面朝斜邊擋風')
(OUT / "lean_to_bare.svg").write_text(svg(s), encoding="utf-8")

# ---------- L 型帳（擋風牆＋屋頂，斜角視圖） ----------
sc = 0.667
def P(x, y):
    return (round(x * sc), round(y * sc))
s = defs()
# ground band
gband = round(752 * sc)
s += f'<rect x="0" y="{gband}" width="{VW}" height="{VH-gband}" fill="{GROUND}" fill-opacity="0.35"/>'
s += f'<line x1="0" y1="{gband}" x2="{VW}" y2="{gband}" stroke="{GROUND}" stroke-width="4"/>'
FLt=P(360,458); FLb=P(360,822); FRt=P(915,458); FRb=P(915,822)
BLt=P(500,300); BLb=P(500,782); BRt=P(1055,300); BRb=P(1055,782)
def pole(t, b):
    return (f'<line x1="{t[0]}" y1="{t[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#3a3f43" stroke-width="10"/>'
            f'<line x1="{t[0]}" y1="{t[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{POLE}" stroke-width="4"/>')
# back wall (windward)
s += f'<path d="M{BLt[0]} {BLt[1]} L{BRt[0]} {BRt[1]} L{BRb[0]} {BRb[1]} L{BLb[0]} {BLb[1]} Z" fill="{WALL}" stroke="{INK}" stroke-width="3"/>'
s += pole(BLt, BLb) + pole(BRt, BRb)
# left side slope panel
s += f'<path d="M{FLt[0]} {FLt[1]} L{BLt[0]} {BLt[1]} L{BLb[0]} {BLb[1]} L{FLb[0]} {FLb[1]} Z" fill="{TARP2}" fill-opacity="0.4" stroke="{INK}" stroke-width="2"/>'
# roof top surface
s += f'<path d="M{FLt[0]} {FLt[1]} L{FRt[0]} {FRt[1]} L{BRt[0]} {BRt[1]} L{BLt[0]} {BLt[1]} Z" fill="{TARP}" fill-opacity="0.85" stroke="{INK}" stroke-width="3"/>'
# front eave poles
s += pole(FLt, FLb) + pole(FRt, FRb)
for b in (FLb, FRb, BLb, BRb):
    s += stake(b[0], b[1])
# guy lines
g1 = P(210, 822); g2 = P(1300, 782)
s += f'<line x1="{FLt[0]}" y1="{FLt[1]}" x2="{g1[0]}" y2="{g1[1]}" stroke="{ROPE}" stroke-width="4" stroke-dasharray="12 8"/>' + stake(g1[0], g1[1])
s += f'<line x1="{BRt[0]}" y1="{BRt[1]}" x2="{g2[0]}" y2="{g2[1]}" stroke="{ROPE}" stroke-width="4" stroke-dasharray="12 8"/>' + stake(g2[0], g2[1])
s += txt(P(778, 250)[0], P(778, 250)[1], '後側兩支＝屋脊柱（高）', GREEN, 21)
s += txt(P(778, 560)[0], P(778, 560)[1], '迎風側立牆', '#ffffff', 20)
s += txt(P(300, 470)[0], P(300, 470)[1], '前側兩支', GREEN, 20)
s += txt(P(300, 508)[0], P(300, 508)[1], '＝屋簷柱（低）', GREEN, 20)
s += cap('兩支登山杖撐起屋頂，迎風側拉低成立牆，四周下釘收緊')
(OUT / "l_shape_bare.svg").write_text(svg(s), encoding="utf-8")

print("Generated:", *[p.name for p in sorted(OUT.glob("*_bare.svg"))])
