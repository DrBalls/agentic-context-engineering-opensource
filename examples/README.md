# ACE Framework Examples

This directory contains practical examples for implementing and experimenting with the Agentic Context Engineering (ACE) framework.

## 📁 Contents

### 1. Minimal ACE Protocol (`minimal_ace_protocol.md`)

**What it is**: A simplified, ready-to-use prompt template that implements the ACE framework
**Best for**: Quick experimentation with any AI assistant (Claude, ChatGPT, etc.)
**Time to try**: 5 minutes

**How to use**:
1. Open the file: `minimal_ace_protocol.md`
2. Copy the entire "Activation Prompt" section
3. Paste it into a new AI chat session
4. Test with the example problems provided

**Expected outcome**: The AI will start responding with explicit Generator → Reflector → Curator phases

---

### 2. Code Implementation (`code/ace_agent.py`)

**What it is**: A Python implementation showing how ACE works programmatically
**Best for**: Understanding the mechanics of ACE and building your own tools
**Time to try**: 2 minutes

**How to run**:
```bash
# From the repository root
python3 examples/code/ace_agent.py
```

**What you'll see**:
- Phase 1: Generator creates 3 solution approaches
- Phase 2: Reflector analyzes trade-offs
- Phase 3: Curator synthesizes recommendations
- Context playbook evolves with learned patterns

**Key insight**: In production, replace the placeholder logic with actual LLM API calls (OpenAI, Anthropic, etc.)

---

## 🎯 Quick Start Guide

### Experiment 1: Protocol-Based (No Coding)

**Goal**: Experience ACE activation firsthand

1. Choose an AI: Claude, ChatGPT, Gemini, etc.
2. Load protocol: Copy contents of `minimal_ace_protocol.md`
3. Paste into new chat session
4. Test with: "Design a notification system for a mobile app"
5. Observe: Look for all three phases in the response

**Success criteria**:
- ✅ Multiple solution approaches (Generator)
- ✅ Trade-off analysis table (Reflector)
- ✅ Clear recommendation (Curator)

---

### Experiment 2: Code-Based (For Developers)

**Goal**: Build ACE into your own tools

1. **Run the example**:
   ```bash
   python3 examples/code/ace_agent.py
   ```

2. **Modify for your use case**:
   - Replace placeholder solutions with LLM API calls
   - Customize the scoring function in `TradeoffAnalysis`
   - Add domain-specific criteria to the Reflector phase

3. **Add persistence**:
   ```python
   import json

   # Save context playbook
   with open('playbook.json', 'w') as f:
       json.dump(agent.get_context_playbook(), f)

   # Load in next session
   with open('playbook.json', 'r') as f:
       playbook = json.load(f)
       agent = ACEAgent(context_playbook=playbook)
   ```

---

## 🔬 Comparison with Full Protocol

| Feature | Minimal Protocol | Full Architect Protocol | Code Implementation |
|---------|------------------|-------------------------|---------------------|
| Complexity | Low | High | Medium |
| Setup time | 30 seconds | 2 minutes | 5 minutes (setup) |
| Effectiveness | Good | Excellent | Depends on LLM integration |
| Customizable | Easy | Moderate | Very flexible |
| Best for | Quick tests | Production use | Building tools |

---

## 🚀 Next Steps

### After trying these examples:

1. **Compare results**: Try the same problem with and without ACE activation
2. **Iterate**: Modify the prompts based on what works for your domain
3. **Share**: If you create an improved version, contribute it back!
4. **Scale**: Integrate into your actual workflow/tools

### Advanced experiments:

- **Multi-turn evolution**: Use ACE across multiple conversations, accumulating insights
- **Domain specialization**: Add domain-specific knowledge to the context playbook
- **Hybrid approach**: Combine prompt-based and code-based methods
- **Cross-system**: Transfer learned patterns between different AI systems

---

## 📚 Resources

### Other ACE Implementations

- **Official Python Implementation**: [kayba-ai/agentic-context-engine](https://github.com/kayba-ai/agentic-context-engine) - Production-ready ACE framework
- **Research Paper**: [arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618) - Original Stanford/Berkeley research
- **Full Protocol**: `../playbooks/awakening/claude_architect.md` - Complete cognitive awakening protocol

### Related Concepts

- **Context Playbooks**: Living documents that evolve with use
- **Delta Updates**: Incremental improvements vs full rewrites
- **Meta-cognitive Prompting**: Prompts that make AI reflect on its own reasoning

---

## 🤝 Contributing

Found an interesting variation? Create a new example file and submit a PR!

**Suggested contributions**:
- Domain-specific protocols (legal, medical, finance, etc.)
- Integration examples (LangChain, AutoGPT, etc.)
- Evaluation metrics for measuring ACE effectiveness
- Multi-agent ACE implementations
