#!/usr/bin/env python3
"""
Quick STORM Research Planner — Community Edition
Lightweight CLI tool to generate multi-perspective research questions and outlines
based on the Stanford STORM protocol.
Part of Deep Research Engine by AntiGravity Studio.
"""

import argparse
import sys

PERSONA_ARCHETYPES = {
    "technical": [
        ("Senior Systems Architect", "Evaluates scalability, latency, failure domains, and distributed state."),
        ("Security & Compliance Lead", "Identifies threat vectors, zero-trust boundaries, data leakage, and regulatory compliance (GDPR, SOC2)."),
        ("FinOps & Infrastructure Engineer", "Analyzes cost curves, compute overhead, storage economics, and operational ROI.")
    ],
    "business": [
        ("Chief Product Officer", "Evaluates customer value, user friction, time-to-market, and competitive moats."),
        ("Risk & Legal Officer", "Scrutinizes contractual obligations, liability, and platform dependencies."),
        ("Growth & Monetization Lead", "Focuses on pricing strategy, distribution leverage, and unit economics.")
    ]
}

def generate_plan(topic: str, domain: str = "technical") -> str:
    personas = PERSONA_ARCHETYPES.get(domain, PERSONA_ARCHETYPES["technical"])
    
    plan = f"""# 🔬 STORM Deep Research Plan: {topic}

> Generated via Quick STORM Planner (Community Edition)
> Architecture: Multi-Perspective Synthesis & Stanford STORM Protocol

## 👥 Simulated Expert Personas:
"""
    for title, focus in personas:
        plan += f"- **{title}**: {focus}\n"
        
    plan += f"""
---

## 📋 Phase 1: Foundational Outline & Scope
1. Core Architectural / Domain Hypotheses
2. Baseline Assumptions to Stress-Test
3. Hard Constraints & Boundary Conditions

## 🔍 Phase 2: Multi-Perspective Interrogation
"""
    for title, _ in personas:
        plan += f"### Perspective: {title}\n"
        plan += f"- Critical Premise: Why might our baseline assumption fail under {title.lower()} constraints?\n"
        plan += f"- Key Trade-Off: What hidden friction or cost does this decision introduce?\n"
        plan += f"- Devil's Advocate Challenge: What is the worst-case failure mode?\n\n"

    plan += """## 📊 Phase 3: Synthesis & Actionable Blueprint
- Resolving conflicting perspectives into concrete recommendations.
- Step-by-step implementation sequence.
- Objective verification metrics and go/no-go gates.

---
💡 *Upgrade to Deep Research Engine Pro for 5-layer drill-down, automated agent orchestration, and KaTeX publication reports.*
"""
    return plan

def main():
    parser = argparse.ArgumentParser(description="Quick Stanford STORM Research Planner (Community Edition)")
    parser.add_argument("topic", nargs="?", help="Topic or architecture to investigate")
    parser.add_argument("--domain", choices=["technical", "business"], default="technical", help="Perspective archetype")
    
    args = parser.parse_args()
    
    if not args.topic:
        print("Usage: python3 quick_storm_planner.py \"Topic to research\" [--domain technical|business]")
        sys.exit(1)
        
    print(generate_plan(args.topic, args.domain))

if __name__ == "__main__":
    main()
