---
name: ip-idea-diversifier
description: Turn a technical or content problem into a diverse, structured IP idea portfolio. Combines solution-space stratification, Verbalized Sampling, semantic deduplication, technical-effect analysis, prior-art challenge questions, and patent-document handoff. Use for invention harvesting, R&D ideation, patent candidate discovery, design-around exploration, or research hypothesis generation.
---

# IP Idea Diversifier

## Scope

This skill supports invention discovery and documentation. It does not provide a legal patentability opinion.

## Required Inputs

- domain
- technical_problem
- target_user_or_environment
- current_solution_and_limitations
- hard_constraints
- excluded_approaches
- available_assets
- desired_technical_effect
- known_prior_art, optional
- target_jurisdiction, optional

## Procedure

1. Convert the brief into problem-cause-constraint-effect form.
2. State up to three conventional baseline approaches.
3. Build 4-8 solution strata, such as physical structure, sensing/data, control, interaction, workflow, safety, modularity, or maintenance.
4. Run stratified balanced VS for the first pass.
5. Run tail VS only on promising underexplored strata.
6. Remove semantic duplicates across all batches.
7. For each candidate, separate:
   - technical problem
   - essential components
   - component relationships
   - operation sequence
   - differentiating mechanism
   - technical effect
   - minimal embodiment
   - alternatives
8. Apply the quality gate.
9. Apply a novelty challenger that explains why the idea may still be known or obvious.
10. Select a portfolio, not a single winner.
11. Produce prior-art search terms and claim seeds.

## Candidate Fields

- title
- one_line_definition
- problem
- mechanism
- components
- operation
- technical_effect
- typicality_estimate
- stratum
- novelty_axes
- implementation_path
- prior_art_collision_hypotheses
- search_keywords
- independent_claim_seed
- dependent_variations
- validation_experiment
- risks

## Selection Rules

- Never select only by low typicality.
- A tail candidate must meet minimum relevance, feasibility, and technical-effect scores.
- Preserve at least two distinct solution strata in the final portfolio.
- Mark business-only ideas lacking a technical mechanism.
- Mark mere aggregation, automation, or UI changes that lack a new technical effect.

## Legal/Research Warning

Low model-estimated typicality does not establish novelty, inventive step, non-obviousness, freedom to operate, or registrability. A prior-art search and qualified review remain mandatory.

## Output

Produce:

1. normalized brief
2. baseline map
3. strata map
4. candidate portfolio
5. rejection/merge log
6. prior-art search plan
7. invention cards for selected candidates
