#!/usr/bin/env python3
"""
ACE Framework Implementation Example
Demonstrates the Generator-Reflector-Curator cycle programmatically
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum


class Phase(Enum):
    GENERATOR = "generator"
    REFLECTOR = "reflector"
    CURATOR = "curator"


@dataclass
class Solution:
    """A proposed solution from the Generator phase"""
    name: str
    description: str
    implementation_steps: List[str]
    assumptions: List[str]

    def __str__(self):
        steps = '\n  '.join(f"{i+1}. {step}" for i, step in enumerate(self.implementation_steps))
        assumptions_str = '\n  - '.join(self.assumptions)
        return f"""
### {self.name}
Description: {self.description}
Steps:
  {steps}
Assumptions:
  - {assumptions_str}
"""


@dataclass
class TradeoffAnalysis:
    """Analysis from the Reflector phase"""
    solution_name: str
    performance: str  # High/Medium/Low
    maintainability: str
    security: str
    cost: str
    risks: List[str]

    def score(self) -> int:
        """Simple scoring for ranking"""
        score_map = {"high": 3, "medium": 2, "low": 1}
        return (
            score_map.get(self.performance.lower(), 0) +
            score_map.get(self.maintainability.lower(), 0) +
            score_map.get(self.security.lower(), 0) +
            (4 - score_map.get(self.cost.lower(), 2))  # Lower cost is better
        )


@dataclass
class CuratedRecommendation:
    """Final output from the Curator phase"""
    primary_choice: str
    rationale: str
    alternative: str
    implementation_guidance: List[str]
    patterns_learned: List[str]


class ACEAgent:
    """
    An agent that implements the ACE framework
    """

    def __init__(self, context_playbook: Dict = None):
        """
        Initialize with an optional context playbook

        Args:
            context_playbook: Accumulated knowledge from previous iterations
        """
        self.context_playbook = context_playbook or {
            "successful_patterns": [],
            "common_pitfalls": [],
            "domain_knowledge": []
        }
        self.current_phase = None
        self.solutions = []
        self.analyses = []
        self.recommendation = None

    def generator_phase(self, problem: str) -> List[Solution]:
        """
        Phase 1: Generate multiple solution approaches

        In a real implementation, this would call an LLM with a generator prompt
        """
        self.current_phase = Phase.GENERATOR
        print("=" * 60)
        print("PHASE 1: GENERATOR - Generating Solutions")
        print("=" * 60)

        # This is a simplified example. In practice, you'd use an LLM here
        # with a prompt that includes the context playbook

        print(f"\nProblem: {problem}")
        print("\nGenerating multiple solution approaches...")
        print("(In production: This calls LLM with Generator prompt + context playbook)")

        # Placeholder: In reality, LLM would generate these
        self.solutions = [
            Solution(
                name="Solution A - Simple In-Memory Queue",
                description="Use Python's built-in queue.Queue with threading",
                implementation_steps=[
                    "Import queue and threading modules",
                    "Create a Queue instance",
                    "Start worker threads that consume from queue",
                    "Add tasks via queue.put()"
                ],
                assumptions=[
                    "Single server deployment",
                    "Tasks complete quickly (< 1 minute)",
                    "OK to lose tasks on restart"
                ]
            ),
            Solution(
                name="Solution B - Redis-backed Queue",
                description="Use Redis with a worker pool for persistence",
                implementation_steps=[
                    "Set up Redis server",
                    "Use rq (Redis Queue) library",
                    "Define task functions with @job decorator",
                    "Start worker processes"
                ],
                assumptions=[
                    "Redis infrastructure available",
                    "Need task persistence",
                    "Multiple workers possible"
                ]
            ),
            Solution(
                name="Solution C - Cloud Queue Service",
                description="Use AWS SQS or Google Cloud Tasks",
                implementation_steps=[
                    "Configure cloud provider credentials",
                    "Create queue in cloud console",
                    "Use SDK to send/receive messages",
                    "Deploy workers as serverless functions"
                ],
                assumptions=[
                    "Cloud budget available",
                    "Need high scalability",
                    "OK with vendor lock-in"
                ]
            )
        ]

        for solution in self.solutions:
            print(solution)

        return self.solutions

    def reflector_phase(self, solutions: List[Solution]) -> List[TradeoffAnalysis]:
        """
        Phase 2: Reflect on solutions with meta-cognitive analysis

        In a real implementation, this would call an LLM with a reflector prompt
        """
        self.current_phase = Phase.REFLECTOR
        print("\n" + "=" * 60)
        print("PHASE 2: REFLECTOR - Analyzing Trade-offs")
        print("=" * 60)

        print("\n(In production: This calls LLM with Reflector prompt + solutions)")

        # Placeholder: In reality, LLM would analyze these
        self.analyses = [
            TradeoffAnalysis(
                solution_name="Solution A",
                performance="High",
                maintainability="Medium",
                security="Medium",
                cost="Low",
                risks=[
                    "Tasks lost on server restart",
                    "No built-in retry mechanism",
                    "Difficult to scale horizontally"
                ]
            ),
            TradeoffAnalysis(
                solution_name="Solution B",
                performance="High",
                maintainability="High",
                security="High",
                cost="Medium",
                risks=[
                    "Redis becomes single point of failure",
                    "Need to manage Redis infrastructure",
                    "Network latency to Redis"
                ]
            ),
            TradeoffAnalysis(
                solution_name="Solution C",
                performance="Medium",
                maintainability="High",
                security="High",
                cost="High",
                risks=[
                    "Vendor lock-in",
                    "Cold start latency for serverless",
                    "Cost can spike with high volume"
                ]
            )
        ]

        print("\n### Trade-off Matrix")
        print(f"{'Solution':<15} {'Perf':<8} {'Maintain':<10} {'Security':<10} {'Cost':<8} {'Score':<6}")
        print("-" * 70)
        for analysis in self.analyses:
            print(f"{analysis.solution_name:<15} {analysis.performance:<8} "
                  f"{analysis.maintainability:<10} {analysis.security:<10} "
                  f"{analysis.cost:<8} {analysis.score():<6}")

        print("\n### Risk Assessment")
        for analysis in self.analyses:
            print(f"\n{analysis.solution_name} Risks:")
            for risk in analysis.risks:
                print(f"  - {risk}")

        return self.analyses

    def curator_phase(self, solutions: List[Solution],
                      analyses: List[TradeoffAnalysis]) -> CuratedRecommendation:
        """
        Phase 3: Curate insights and provide recommendations

        In a real implementation, this would call an LLM with a curator prompt
        """
        self.current_phase = Phase.CURATOR
        print("\n" + "=" * 60)
        print("PHASE 3: CURATOR - Synthesizing Recommendation")
        print("=" * 60)

        print("\n(In production: This calls LLM with Curator prompt + solutions + analyses)")

        # Rank solutions by score
        ranked = sorted(
            zip(solutions, analyses),
            key=lambda x: x[1].score(),
            reverse=True
        )

        best_solution, best_analysis = ranked[0]
        second_best_solution, second_best_analysis = ranked[1]

        self.recommendation = CuratedRecommendation(
            primary_choice=best_solution.name,
            rationale=f"Best balance of {best_analysis.performance.lower()} performance, "
                     f"{best_analysis.maintainability.lower()} maintainability, and "
                     f"{best_analysis.cost.lower()} cost",
            alternative=f"{second_best_solution.name} - Use if you need "
                       f"{second_best_analysis.security.lower()} security",
            implementation_guidance=[
                f"Start with: {best_solution.implementation_steps[0]}",
                f"Monitor for: Task processing latency, queue depth",
                f"Pivot if: {best_analysis.risks[0]}"
            ],
            patterns_learned=[
                "Simple solutions often best for MVP",
                "Consider operational complexity in trade-offs",
                "Start simple, migrate to complex as needed"
            ]
        )

        print(f"\n### Recommendation")
        print(f"**Primary Choice:** {self.recommendation.primary_choice}")
        print(f"**Rationale:** {self.recommendation.rationale}")
        print(f"\n**Alternative:** {self.recommendation.alternative}")

        print(f"\n### Implementation Guidance")
        for guidance in self.recommendation.implementation_guidance:
            print(f"  - {guidance}")

        print(f"\n### Patterns Learned (Delta Updates to Playbook)")
        for pattern in self.recommendation.patterns_learned:
            print(f"  - {pattern}")
            # Update context playbook with new patterns
            if pattern not in self.context_playbook["successful_patterns"]:
                self.context_playbook["successful_patterns"].append(pattern)

        return self.recommendation

    def process_task(self, problem: str) -> CuratedRecommendation:
        """
        Execute the complete ACE cycle: Generator -> Reflector -> Curator
        """
        print("\n" + "🔄" * 30)
        print("ACE FRAMEWORK EXECUTION")
        print("🔄" * 30)

        # Phase 1: Generate solutions
        solutions = self.generator_phase(problem)

        # Phase 2: Reflect on trade-offs
        analyses = self.reflector_phase(solutions)

        # Phase 3: Curate recommendations
        recommendation = self.curator_phase(solutions, analyses)

        print("\n" + "✅" * 30)
        print("ACE CYCLE COMPLETE")
        print("✅" * 30)
        print(f"\nContext Playbook now contains {len(self.context_playbook['successful_patterns'])} patterns")

        return recommendation

    def get_context_playbook(self) -> Dict:
        """Return the accumulated context playbook"""
        return self.context_playbook


def main():
    """Demonstrate the ACE framework in action"""

    # Initialize agent with empty context
    agent = ACEAgent()

    # Process a task
    problem = "Design a task queue system for a web application that processes user uploads"

    recommendation = agent.process_task(problem)

    # Show evolved context
    print("\n" + "=" * 60)
    print("EVOLVED CONTEXT PLAYBOOK")
    print("=" * 60)
    print("\nSuccessful Patterns:")
    for pattern in agent.get_context_playbook()["successful_patterns"]:
        print(f"  ✓ {pattern}")

    print("\n💡 Key Insight: The context playbook evolves with each task!")
    print("   In production, this playbook would be persisted and reused")
    print("   across sessions, making the agent progressively smarter.\n")


if __name__ == "__main__":
    main()
