#!/usr/bin/env python3
"""Wraps src/app.html into a standalone, installable index.html."""
import pathlib
root = pathlib.Path(__file__).parent
app = (root / "src/app.html").read_text()
head = """<!doctype html>
<html lang="en" data-standalone="1">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Drape">
<meta name="theme-color" content="#eef0f3">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head>
<body>
"""
(root / "index.html").write_text(head + app + "\n</body>\n</html>\n")
print("wrote index.html")
