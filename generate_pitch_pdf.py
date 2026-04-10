#!/usr/bin/env python3
"""Generate pitch deck PDF in brutalist dark style."""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Page setup
W, H = landscape(A4)
OUT = os.path.join(os.path.dirname(__file__), "website", "pitch-deck.pdf")

# Colors
BG = HexColor("#0A0A0A")
CARD = HexColor("#161616")
BORDER = HexColor("#2A2A2A")
GRAY = HexColor("#666666")
LGRAY = HexColor("#999999")
WHITE = HexColor("#FFFFFF")
RED = HexColor("#FF3B3B")
GREEN = HexColor("#00E676")

def draw_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def draw_card(c, x, y, w, h, fill=CARD, border=BORDER):
    c.setFillColor(fill)
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setStrokeColor(border)
    c.setLineWidth(0.5)
    c.rect(x, y, w, h, fill=0, stroke=1)

def draw_label(c, x, y, text):
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(x, y, text)

def draw_slide_num(c, num, total):
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawString(30, 20, f"{num:02d} / {total:02d}")
    # progress bar
    c.setStrokeColor(RED)
    c.setLineWidth(2)
    prog_w = W * (num / total)
    c.line(0, H, prog_w, H)

M = 50  # margin

# =============================================
# SLIDE 1: Title
# =============================================
def slide_01(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[01] INTRODUCTION")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 58)
    c.drawString(M, H - 160, "Go-to-Market")

    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 58)
    c.drawString(M, H - 230, "Airdrop")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 58)
    c.drawString(M, H - 300, "Campaigns")

    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 14)
    c.drawString(M, H - 360, "One product. One specialization. Predictable results.")

    draw_slide_num(c, 1, 12)

# =============================================
# SLIDE 2: Problem
# =============================================
def slide_02(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[02] THE PROBLEM")

    cards = [
        ("[01]", "No ROI", "$50-100K+ spent on marketing\nwith no clear return"),
        ("[02]", "Bots, Not Users", "Airdrop attracted bots.\nZero real product traction."),
        ("[03]", "Fragmented Team", "5-7 freelancers with no sync.\nSMM says one thing, KOL another."),
        ("[04]", "Dead Community", "Community dies 2 weeks after\ncampaign. No retention."),
    ]

    cw = (W - M * 2 - 10) / 2
    ch = (H - 120 - 10) / 2
    for i, (num, title, desc) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = M + col * (cw + 10)
        y = H - 100 - (row + 1) * (ch + 10) + 10
        draw_card(c, x, y, cw, ch)

        c.setFillColor(GRAY)
        c.setFont("Helvetica", 8)
        c.drawString(x + 20, y + ch - 30, num)

        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(x + 20, y + ch - 65, title)

        c.setFillColor(LGRAY)
        c.setFont("Helvetica", 11)
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            c.drawString(x + 20, y + ch - 90 - j * 16, line)

    draw_slide_num(c, 2, 12)

# =============================================
# SLIDE 3: Insight
# =============================================
def slide_03(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[03] INSIGHT")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(M, H - 150, "Airdrop is not marketing.")

    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(M, H - 200, "It's a product launch.")

    items = ["Real users who\nuse the product", "Metrics for\ninvestors", "Community\nthat stays", "Measurable\nROI"]
    iw = (W - M * 2 - 30) / 4
    y_base = H - 320
    for i, item in enumerate(items):
        x = M + i * (iw + 10)
        # top line
        c.setStrokeColor(BORDER)
        c.setLineWidth(1.5)
        c.line(x, y_base + 40, x + iw, y_base + 40)
        c.setFillColor(LGRAY)
        c.setFont("Helvetica", 12)
        lines = item.split("\n")
        for j, line in enumerate(lines):
            c.drawString(x, y_base + 18 - j * 16, line)

    draw_slide_num(c, 3, 12)

# =============================================
# SLIDE 4: What We Do
# =============================================
def slide_04(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[04] WHAT WE DO")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 36)
    text = "Turnkey go-to-market"
    tw = c.stringWidth(text, "Helvetica-Bold", 36)
    c.drawString((W - tw) / 2, H - 170, text)
    text2 = "airdrop campaigns"
    tw2 = c.stringWidth(text2, "Helvetica-Bold", 36)
    c.drawString((W - tw2) / 2, H - 215, text2)

    # Flow
    steps = ["Prep", "Season 1", "Season 2", "..."]
    total_w = len(steps) * 130 + (len(steps) - 1) * 40
    sx = (W - total_w) / 2
    sy = H - 310
    for i, step in enumerate(steps):
        x = sx + i * 170
        draw_card(c, x, sy, 130, 45)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14)
        stw = c.stringWidth(step, "Helvetica-Bold", 14)
        c.drawString(x + (130 - stw) / 2, sy + 17, step)
        if i < len(steps) - 1:
            c.setFillColor(GRAY)
            c.setFont("Helvetica", 18)
            c.drawString(x + 145, sy + 14, "→")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 12)
    note = "Strategy, quest mechanics, funnel, content, traffic, community, social media — all under one roof."
    nw = c.stringWidth(note, "Helvetica", 12)
    c.drawString((W - nw) / 2, sy - 50, note)

    draw_slide_num(c, 4, 12)

# =============================================
# SLIDE 5: Case Nomisma
# =============================================
def slide_05(c):
    draw_bg(c)

    # Left side
    draw_label(c, M, H - 60, "[05] CASE STUDY")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(M, H - 130, "Nomisma Network")

    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 13)
    c.drawString(M, H - 160, "Blockchain Ecosystem — Backed by Chromia")

    c.setStrokeColor(BORDER)
    c.line(M, H - 190, W / 2 - 30, H - 190)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(M, H - 215, "Start: Project not launched. Community = 0. Awareness = 0.")
    c.drawString(M, H - 235, "Feb 2025 — Present")

    # Right side — metric cards
    rx = W / 2 + 10
    metrics = [
        ("TELEGRAM", "20K"),
        ("DISCORD", "30K"),
        ("TWITTER", "27K"),
        ("PARTICIPANTS", "65K"),
        ("QUESTS DONE", "2M"),
        ("NID MINTED ($10)", "9,500"),
    ]
    cw = (W - rx - M - 6) / 2
    ch = 62
    for i, (label, value) in enumerate(metrics):
        col = i % 2
        row = i // 2
        x = rx + col * (cw + 6)
        y = H - 80 - (row + 1) * (ch + 6) + 6
        draw_card(c, x, y, cw, ch)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 7)
        c.drawString(x + 12, y + ch - 18, label)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(x + 12, y + 12, value)

    # ROI card — red
    roi_y = H - 80 - 4 * (ch + 6) + 6
    roi_w = 2 * cw + 6
    draw_card(c, rx, roi_y, roi_w, ch, fill=RED, border=RED)
    c.setFillColor(HexColor("#FFaaaa"))
    c.setFont("Helvetica", 7)
    c.drawString(rx + 12, roi_y + ch - 18, "MARKETING ROI")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(rx + 12, roi_y + 12, "500%")

    draw_slide_num(c, 5, 12)

# =============================================
# SLIDE 6: Case NDA
# =============================================
def slide_06(c):
    draw_bg(c)

    draw_label(c, M, H - 60, "[06] CASE STUDY")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(M, H - 130, "[NDA] Trading Platform")

    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 13)
    c.drawString(M, H - 160, "Trading Aggregator")

    c.setStrokeColor(BORDER)
    c.line(M, H - 190, W / 2 - 30, H - 190)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(M, H - 215, "Start: MVP product, zero users, zero trading volume.")
    c.drawString(M, H - 235, "Dec 2025 — Apr 2026")

    rx = W / 2 + 10
    metrics = [
        ("DISCORD", "50K"),
        ("TWITTER", "60K"),
        ("TELEGRAM", "20K"),
        ("PARTICIPANTS", "50K"),
    ]
    cw = (W - rx - M - 6) / 2
    ch = 62
    for i, (label, value) in enumerate(metrics):
        col = i % 2
        row = i // 2
        x = rx + col * (cw + 6)
        y = H - 80 - (row + 1) * (ch + 6) + 6
        draw_card(c, x, y, cw, ch)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 7)
        c.drawString(x + 12, y + ch - 18, label)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(x + 12, y + 12, value)

    # Traction card
    tr_y = H - 80 - 3 * (ch + 6) + 6
    tr_w = 2 * cw + 6
    draw_card(c, rx, tr_y, tr_w, ch)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawString(rx + 12, tr_y + ch - 18, "PRODUCT TRACTION")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(rx + 12, tr_y + 12, "First Trading Volume")

    # Bonus card
    bn_y = tr_y - ch - 6
    draw_card(c, rx, bn_y, tr_w, ch, fill=HexColor("#111111"))
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawString(rx + 12, bn_y + ch - 18, "BONUS")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 12)
    c.drawString(rx + 12, bn_y + 14, "Ambassador Program + Organic Twitter Publications")

    draw_slide_num(c, 6, 12)

# =============================================
# SLIDE 7: Pattern
# =============================================
def slide_07(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[07] PATTERN")

    pw = (W - M * 2 - 10) / 2
    ph = 200

    # Nomisma
    draw_card(c, M, H - 80 - ph, pw, ph)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(M + 20, H - 110, "Nomisma Network")
    stats_n = [("Start", "From zero"), ("Community", "0 → 77K"), ("Participants", "65K"), ("Traction", "9,500 paid mints")]
    for i, (lab, val) in enumerate(stats_n):
        y = H - 145 - i * 30
        c.setStrokeColor(BORDER)
        c.line(M + 20, y - 8, M + pw - 20, y - 8)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(M + 20, y, lab)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawRightString(M + pw - 20, y, val)

    # NDA
    draw_card(c, M + pw + 10, H - 80 - ph, pw, ph)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(M + pw + 30, H - 110, "[NDA] Trading Aggregator")
    stats_t = [("Start", "From zero"), ("Community", "0 → 130K"), ("Participants", "50K"), ("Traction", "First volume")]
    for i, (lab, val) in enumerate(stats_t):
        y = H - 145 - i * 30
        c.setStrokeColor(BORDER)
        c.line(M + pw + 30, y - 8, M + 2 * pw - 10, y - 8)
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(M + pw + 30, y, lab)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawRightString(M + 2 * pw - 10, y, val)

    # Bottom banner
    bh = 80
    by = H - 100 - ph - 20 - bh
    draw_card(c, M, by, W - M * 2, bh, border=RED)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 16)
    t1 = "Everyone does airdrop campaigns. For everyone it's one service out of ten."
    tw1 = c.stringWidth(t1, "Helvetica-Bold", 16)
    c.drawString((W - tw1) / 2, by + bh - 32, t1)
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 18)
    t2 = "We only do this. One product. One specialization."
    tw2 = c.stringWidth(t2, "Helvetica-Bold", 18)
    c.drawString((W - tw2) / 2, by + 18, t2)

    draw_slide_num(c, 7, 12)

# =============================================
# SLIDE 8: Process
# =============================================
def slide_08(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[08] PROCESS")

    steps = [
        ("01", "Preparation", "1-2 WEEKS", "Product & audience analysis.\nStrategy. Quest mechanics.\nChannel setup. Funnel design."),
        ("02", "Season", "2-4 MONTHS", "Campaign launch. Content,\ntraffic, community, quests.\nWeekly reports. Optimization."),
        ("03", "Next Season", "ONGOING", "Results analysis. Strategy\nadjustment. New wave.\nScale what worked."),
    ]

    cw = (W - M * 2 - 20) / 3
    ch = H - 130
    for i, (num, title, time, desc) in enumerate(steps):
        x = M + i * (cw + 10)
        y = 40
        draw_card(c, x, y, cw, ch)

        c.setFillColor(BORDER)
        c.setFont("Helvetica-Bold", 48)
        c.drawString(x + 20, y + ch - 70, num)

        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(x + 20, y + ch - 105, title)

        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x + 20, y + ch - 125, time)

        c.setFillColor(LGRAY)
        c.setFont("Helvetica", 11)
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            c.drawString(x + 20, y + 60 - j * 16, line)

    draw_slide_num(c, 8, 12)

# =============================================
# SLIDE 9: Results
# =============================================
def slide_09(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[09] WHAT YOU GET")

    items = [
        ("200%+", "Predicted ROI\n(Nomisma: 500%)", True),
        ("20-60K", "Campaign\nparticipants", False),
        ("50K+", "Community members\nacross channels", False),
        ("✓", "Product traction —\nreal users, transactions", False),
        ("✓", "Packed social media\nwith regular content", False),
        ("✓", "Weekly reports —\nfull transparency", False),
    ]

    cw = (W - M * 2 - 20) / 3
    ch = (H - 130) / 2 - 5
    for i, (num, label, accent) in enumerate(items):
        col = i % 3
        row = i // 3
        x = M + col * (cw + 10)
        y = H - 90 - (row + 1) * (ch + 10) + 10
        fill = RED if accent else CARD
        draw_card(c, x, y, cw, ch, fill=fill)

        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 32)
        c.drawString(x + 20, y + ch - 50, num)

        c.setFillColor(HexColor("#FFaaaa") if accent else LGRAY)
        c.setFont("Helvetica", 11)
        lines = label.split("\n")
        for j, line in enumerate(lines):
            c.drawString(x + 20, y + 25 - j * 15, line)

    draw_slide_num(c, 9, 12)

# =============================================
# SLIDE 10: Pricing
# =============================================
def slide_10(c):
    draw_bg(c)

    bw = (W - M * 2 - 20) / 3
    bh = H - 100

    # Prep
    draw_card(c, M, 40, bw, bh)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(M + 25, 40 + bh - 30, "[01] PREPARATION")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 12)
    c.drawString(M + 25, 40 + bh - 60, "Strategy, setup, funnel")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(M + 25, 40 + bh - 115, "$5-7K")
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(M + 25, 40 + bh - 140, "one-time")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 10)
    desc1 = ["Product analysis. Campaign", "mechanics. Channel setup.", "Quest design. Traffic funnel."]
    for j, line in enumerate(desc1):
        c.drawString(M + 25, 40 + 70 - j * 15, line)

    # Season
    x2 = M + bw + 10
    draw_card(c, x2, 40, bw, bh)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(x2 + 25, 40 + bh - 30, "[02] SEASON MANAGEMENT")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 12)
    c.drawString(x2 + 25, 40 + bh - 60, "Launch & run the campaign")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(x2 + 25, 40 + bh - 115, "$3-4K")
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(x2 + 25, 40 + bh - 140, "/month")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 10)
    desc2 = ["Content, traffic, community,", "quests, optimization.", "Weekly reports."]
    for j, line in enumerate(desc2):
        c.drawString(x2 + 25, 40 + 70 - j * 15, line)

    # Compare
    x3 = M + 2 * (bw + 10)
    draw_card(c, x3, 40, bw, bh, fill=HexColor("#111111"))
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(x3 + 25, 40 + bh - 30, "FOR COMPARISON")
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x3 + 25, 40 + bh - 60, "In-house team")
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(x3 + 25, 40 + bh - 115, "$15-25K")
    # strikethrough
    tw = c.stringWidth("$15-25K", "Helvetica-Bold", 32)
    c.setStrokeColor(GRAY)
    c.setLineWidth(2)
    c.line(x3 + 25, 40 + bh - 105, x3 + 25 + tw, 40 + bh - 105)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(x3 + 25, 40 + bh - 140, "/month")
    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 10)
    desc3 = ["SMM + CM + KOL Manager", "+ Designer + PM.", "Salaries only. No strategy.", "No guarantees."]
    for j, line in enumerate(desc3):
        c.drawString(x3 + 25, 40 + 70 - j * 15, line)

    draw_slide_num(c, 10, 12)

# =============================================
# SLIDE 11: How We Work
# =============================================
def slide_11(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[11] HOW WE WORK")

    items = [
        ("Founders work personally", "We don't hand off to juniors. You work\ndirectly with the people who ran\nNomisma and Trading Aggregator."),
        ("Weekly reports", "Full transparency on every metric.\nNo surprises. You see exactly\nwhat's happening."),
        ("Pay per stage", "Preparation is separate. Management\nis monthly. Don't like it —\nstop anytime."),
        ("Your result = our case", "A bad result hurts us just as much.\nOur case studies are our\nmain asset."),
    ]

    cw = (W - M * 2 - 10) / 2
    ch = (H - 130) / 2 - 5
    for i, (title, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        x = M + col * (cw + 10)
        y = H - 90 - (row + 1) * (ch + 10) + 10
        draw_card(c, x, y, cw, ch)

        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 19)
        c.drawString(x + 25, y + ch - 40, title)

        c.setFillColor(LGRAY)
        c.setFont("Helvetica", 12)
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            c.drawString(x + 25, y + ch - 70 - j * 17, line)

    draw_slide_num(c, 11, 12)

# =============================================
# SLIDE 12: CTA
# =============================================
def slide_12(c):
    draw_bg(c)
    draw_label(c, M, H - 60, "[12] NEXT STEP")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 44)
    c.drawString(M, H - 160, "Let's see if this")
    c.drawString(M, H - 215, "is right for you.")

    c.setFillColor(LGRAY)
    c.setFont("Helvetica", 14)
    c.drawString(M, H - 270, "30 minutes. We'll analyze your project and tell you honestly —")
    c.drawString(M, H - 290, "whether an airdrop campaign makes sense and what results to expect.")

    # Contact cards
    contacts = ["Telegram", "Email", "Twitter"]
    cx = M
    for contact in contacts:
        cw_btn = 140
        draw_card(c, cx, H - 370, cw_btn, 45)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(cx + 20, H - 353, contact)
        cx += cw_btn + 15

    draw_slide_num(c, 12, 12)


# =============================================
# GENERATE
# =============================================
def main():
    c = canvas.Canvas(OUT, pagesize=landscape(A4))
    c.setTitle("Go-to-Market Airdrop Campaigns — Pitch Deck")
    c.setAuthor("Zemnevodow")

    slides = [slide_01, slide_02, slide_03, slide_04, slide_05,
              slide_06, slide_07, slide_08, slide_09, slide_10,
              slide_11, slide_12]

    for i, slide_fn in enumerate(slides):
        slide_fn(c)
        if i < len(slides) - 1:
            c.showPage()

    c.save()
    print(f"PDF saved to: {OUT}")
    print(f"Size: {os.path.getsize(OUT) / 1024:.0f} KB")

if __name__ == "__main__":
    main()
