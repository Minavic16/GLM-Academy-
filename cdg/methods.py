"""TaskModel / Method AND-OR structure and prerequisite derivation helpers.

Evaluation rule (frozen): a TaskModel T is satisfiable iff there exists some
Method M of T such that every KC required by M is satisfied.
  - Within a Method: required KCs are ANDed.
  - Across Methods of the same TaskModel: Methods are ORed.
"""
from __future__ import annotations

from typing import Iterable, Mapping, Sequence, Set


def evaluate_task_model(
    methods: Iterable[Iterable[str]], satisfied_kcs: Set[str]
) -> bool:
    methods = list(methods)
    if len(methods) == 0:
        return False
    return any(set(reqs) <= satisfied_kcs for reqs in methods)


def method_is_satisfied(required: Iterable[str], satisfied_kcs: Set[str]) -> bool:
    return set(required) <= satisfied_kcs


def derive_all_scope_execute_prerequisites(
    target_kc: str,
    methods_by_task_model: Mapping[str, Sequence[Sequence[str]]],
    task_models_by_target: Mapping[str, Set[str]],
) -> Set[str]:
    """A is an ALL-scope EXECUTE prerequisite of B iff every Method of every
    TaskModel targeting B requires A. Derivation skips A == B."""
    result: Set[str] = set()
    tms = task_models_by_target.get(target_kc, set())
    if not tms:
        return result
    all_method_sets: list[Set[str]] = []
    for tm in tms:
        methods = methods_by_task_model.get(tm, [])
        if not methods:
            # A TaskModel with no recorded methods contributes no evidence.
            return result
        all_method_sets.extend(set(m) for m in methods)
    if not all_method_sets:
        return result
    common = set.intersection(*all_method_sets)
    common.discard(target_kc)
    return common
