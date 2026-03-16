'use client';

import CurvedLoop from './CurvedLoop';

const FLAGS = '🇲🇦 🇷🇴 🇨🇴 🇪🇨 🇻🇪 🇦🇷 🇵🇪 🇨🇳 🇬🇧 🇮🇹 🇵🇰 🇭🇳 🇩🇴 🇧🇴 🇧🇷 🇸🇳';

export default function GlobeWithFlags() {
  // Globe size in px (reference for positioning the curved text)
  const GLOBE_SIZE = 320;

  return (
    <div
      style={{
        position: 'relative',
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: `${GLOBE_SIZE + 60}px`,
        userSelect: 'none',
      }}
    >
      {/* ── Curved text layer (BEHIND the globe) ── */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 0,
          // Shift the strip slightly below centre so the curve arc
          // aligns with the equator/bottom of the globe
          paddingTop: `${GLOBE_SIZE * 0.28}px`,
        }}
      >
        <CurvedLoop
          marqueeText={FLAGS}
          speed={1.6}
          // curveAmount controls how deep the arc dips.
          // A higher value = deeper curve downward.
          // Tune this so the arc follows the bottom half of the globe.
          curveAmount={210}
          direction="right"
          interactive={false}
        />
      </div>

      {/* ── Globe sphere (ON TOP of the text) ── */}
      <div
        style={{
          position: 'relative',
          zIndex: 1,
          width: GLOBE_SIZE,
          height: GLOBE_SIZE,
          borderRadius: '50%',
          // Multi-layer gradient: gives a 3-D lit sphere look
          background: `
            radial-gradient(circle at 35% 35%,
              rgba(255,255,255,0.18) 0%,
              transparent 55%
            ),
            radial-gradient(circle at 50% 50%,
              #0d2a45 0%,
              #071728 55%,
              #020c17 100%
            )
          `,
          boxShadow: `
            0 0 0 1.5px rgba(100,200,255,0.18),
            0 0 60px 10px rgba(0,80,160,0.35),
            inset 0 0 80px 20px rgba(0,0,0,0.5)
          `,
          overflow: 'hidden',
        }}
      >
        {/* Latitude lines */}
        {[20, 40, 60, 80].map((pct) => (
          <div
            key={pct}
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: `${pct}%`,
              height: '1px',
              background: 'rgba(100,200,255,0.12)',
            }}
          />
        ))}
        {/* Longitude lines */}
        {[20, 40, 60, 80].map((pct) => (
          <div
            key={pct}
            style={{
              position: 'absolute',
              top: 0,
              bottom: 0,
              left: `${pct}%`,
              width: '1px',
              background: 'rgba(100,200,255,0.12)',
            }}
          />
        ))}
        {/* Equator highlight */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: '50%',
            height: '1.5px',
            background: 'rgba(100,220,255,0.30)',
            transform: 'translateY(-50%)',
          }}
        />
        {/* Specular highlight */}
        <div
          style={{
            position: 'absolute',
            top: '12%',
            left: '18%',
            width: '30%',
            height: '22%',
            borderRadius: '50%',
            background:
              'radial-gradient(circle, rgba(255,255,255,0.22) 0%, transparent 80%)',
          }}
        />
      </div>
    </div>
  );
}
