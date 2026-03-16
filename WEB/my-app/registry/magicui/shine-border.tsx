"use client";

import { CSSProperties } from "react";

interface ShineBorderProps {
  shineColor?: string | string[];
  duration?: number;
  borderWidth?: number;
  className?: string;
}

export function ShineBorder({
  shineColor = "#C9A84C",
  duration = 14,
  borderWidth = 1,
  className = "",
}: ShineBorderProps) {
  const colors = Array.isArray(shineColor) ? shineColor.join(",") : shineColor;

  return (
    <div
      className={`pointer-events-none absolute inset-0 rounded-2xl ${className}`}
      style={
        {
          "--shine-color": colors,
          "--duration": `${duration}s`,
          "--border-width": `${borderWidth}px`,
          backgroundImage: `conic-gradient(from var(--angle), transparent 70%, ${colors})`,
          WebkitMask:
            "linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)",
          WebkitMaskComposite: "xor",
          maskComposite: "exclude",
          padding: `${borderWidth}px`,
          animation: `shine-border var(--duration) linear infinite`,
        } as CSSProperties
      }
    />
  );
}
