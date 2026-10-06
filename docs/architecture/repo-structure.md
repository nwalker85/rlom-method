# Repository structure

This repository conforms to **Tier 2** of the Ravenhelm Repository Structure Template. The full template is vendored below for durability — it travels with the repo and does not depend on an external standards file.

The template assembles de facto community standards (GitHub-recognized special files, Standard Readme, Keep a Changelog, Conventional Commits, SemVer, REUSE, OpenSSF, SPDX) into a coherent default. No ISO standard exists for repository structure.

- **Conformance tier:** Tier 2 (production OSS layout). Tier 3 additions deferred — revisit when commercial distribution begins.
- **Origin:** Maintained by Ravenhelm as part of the Ravenhelm Repository Structure Template.
- **Authority over this repo:** This document, then the per-section `CONTRIBUTING.md` and `docs/_shared/CONTEXT.md`. The repo-structure template governs *layout*; CONTEXT governs *content*.

## How this repo conforms

The table below records the decisions this repo made against the template's six explicit decision points, plus the language-overlay and Tier-3 choices.

| Decision point | Choice | Notes |
|---|---|---|
| Monorepo vs polyrepo | Single repo under product | One repo today; siblings (`assessment-toolkit/`, `agent-extensions/`) will live alongside under the RLOM product suite. |
| `deploy/` vs `infra/` | Neither | Docs-only project; no infrastructure to deploy. |
| `docs/` source vs generated | Source only | `build/` is gitignored; single-file edition compiled via `scripts/compile.sh`. |
| ADR location | `docs/architecture/decisions/` | Standard layout. ADRs document doctrine evolution, not code architecture. |
| CODEOWNERS placement | Repo root | More discoverable than `.github/CODEOWNERS`. |
| CI provider | GitHub Actions | `.github/workflows/lint.yml` runs markdownlint and a chapter-rubric check. |
| Language overlay | None | Markdown-only repo; no language manifest. |
| Tier-3 additions | Deferred | `THIRDPARTY.md`, `SBOM.spdx.json`, `REUSE.toml`, `governance/` skipped until commercial distribution. |

## How new repos under this product should conform

Future repos under the RLOM product suite (assessment toolkit, agent extensions, etc.) should adopt the template at the tier appropriate to their nature:

- **Docs / spec repos** — Tier 2, as this one.
- **Library / SDK repos** — Tier 2, plus the language overlay table at the bottom.
- **Service / deployable repos** — Tier 2, plus `deploy/` (not `infra/` — pick one and be consistent across the product).
- **Anything shipping under contractual SLA** — promote to Tier 3.

---

# Repository Structure Template

A pragmatic layout for production-grade repositories. Language-agnostic at the root; language-specific conventions overlay below. No ISO standard exists for repository structure — this template assembles the de facto community standards (GitHub-recognized special files, Standard Readme, Keep a Changelog, Conventional Commits, SemVer, REUSE, OpenSSF, SPDX) into a coherent default.

---

## Tier 1 — Minimal (any OSS project)

```
project-root/
├── README.md                       # Front door — concise positioning + quick start
├── LICENSE                         # SPDX identifier in filename or header
├── .gitignore
└── src/                            # or language-native equivalent
    └── ...
```

## Tier 2 — Standard (production OSS)

```
project-root/
│
│  # Root-level metadata (GitHub-recognized [GH] or community standards)
├── README.md                       # [GH] Project front door
├── LICENSE                         # [GH] SPDX-identified, machine-readable
├── CHANGELOG.md                    # [Keep a Changelog] release notes
├── CONTRIBUTING.md                 # [GH] PR process, dev setup, style guide
├── CODE_OF_CONDUCT.md              # [GH] expected behavior
├── SECURITY.md                     # [GH] vulnerability disclosure policy
├── CODEOWNERS                      # [GH] review routing (or in .github/)
├── .gitignore
├── .gitattributes                  # line endings, LFS rules
├── .editorconfig                   # cross-editor formatting consistency
│
│  # CI/CD and platform metadata
├── .github/                        # [GH] platform-specific
│   ├── workflows/                  # GitHub Actions pipelines
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml              # supply-chain auto-updates
│   └── FUNDING.yml                 # [GH] sponsorship links
│
│  # Source
├── src/                            # primary source (or language-native: cmd/+pkg/, etc.)
├── tests/                          # tests (often co-located with src per language)
├── examples/                       # usage samples
│
│  # Documentation
├── docs/
│   ├── architecture/
│   │   ├── README.md               # architecture overview
│   │   ├── decisions/              # ADRs (Architecture Decision Records)
│   │   └── diagrams/               # C4, sequence, deployment
│   ├── api/                        # OpenAPI / AsyncAPI / GraphQL specs
│   ├── guides/                     # how-tos, tutorials
│   └── runbooks/                   # operational procedures
│
│  # Infrastructure & operations
├── deploy/                         # or infra/ — choose one and be consistent
│   ├── docker/                     # Dockerfiles
│   ├── compose/                    # docker-compose for local dev
│   ├── helm/                       # Helm charts
│   └── terraform/                  # IaC
│
├── scripts/                        # bootstrap, dev, ops scripts
├── tools/                          # internal tooling
│
└── <language-manifest>             # pyproject.toml | go.mod | Cargo.toml | package.json | pom.xml
```

## Tier 3 — Enterprise / Regulated additions

Add to Tier 2 when the project ships under audit, regulatory scope, or contractual SLA:

```
project-root/
│
├── SBOM.spdx.json                  # [SPDX / ISO 5962] software bill of materials (generated)
├── THIRDPARTY.md                   # third-party license attribution
├── NOTICES                         # Apache-style notice file if required
├── REUSE.toml                      # [REUSE] machine-readable licensing per file
│
├── governance/
│   ├── RACI.md                     # roles and accountability
│   ├── policies/                   # security, data, privacy policies
│   └── evidence/                   # audit artifacts (often gitignored, externally stored)
│
└── conformance.yaml                # EPAS v2.0 conformance state (if EPAS-aligned)
```

---

## Language-specific overlays

| Language | Convention | Notes |
|---|---|---|
| Python | `src/<package>/` layout per PEP 621 | `src/` layout preferred over flat — prevents accidental imports from cwd |
| Go | `cmd/<binary>/`, `pkg/<lib>/`, `internal/<private>/` | `golang-standards/project-layout` is community, not official |
| Rust | `src/`, `tests/`, `examples/`, `benches/` | Cargo enforces; deviation rarely productive |
| Java / Kotlin | `src/main/<lang>/`, `src/test/<lang>/` | Maven Standard Directory Layout |
| TypeScript / Node | `src/`, `dist/` (gitignored), `node_modules/` (gitignored) | Workspace tooling (pnpm/Turbo/Nx) adds `packages/` |
| Monorepo | `packages/<service>/`, `libs/<shared>/` | Each package internally follows its language convention |

---

## Decision points (make these explicit before scaffolding)

1. **Monorepo vs polyrepo** — affects whether `packages/` lives at root
2. **`deploy/` vs `infra/`** — pick one term and use it everywhere
3. **`docs/` source vs generated** — if you publish a docs site, separate source (`docs/`) from build output (`site/`, gitignored)
4. **ADR location** — `docs/architecture/decisions/` is standard; some teams prefer `decisions/` at root for visibility
5. **CODEOWNERS placement** — root or `.github/`; GitHub honors both, root is more discoverable
6. **CI provider** — `.github/workflows/`, `.gitlab-ci.yml`, `.circleci/`, `azure-pipelines.yml`; commit to one

---

## Anti-patterns

- Deep nesting beyond 4 levels — discourages navigation
- Multiple competing source directories at the same level (`src/` + `lib/` + `app/`) — pick one
- Build artifacts in version control (`dist/`, `target/`, `node_modules/`)
- Secrets or credentials anywhere in the tree (including `.env` files)
- Personal IDE configuration in repo root (use `.editorconfig`, not `.vscode/settings.json`)
- Repository-wide README that documents internals instead of pointing at them
- Mixing concerns at root (no `old_backup/`, `temp/`, `WIP/`)

---

## Minimum viable file contents

Every Tier 2+ repository should have these files non-empty:

- **README.md** — what it is, why it exists, how to install, how to run tests, where to find docs
- **LICENSE** — full text, not just a reference
- **CHANGELOG.md** — at minimum, an `[Unreleased]` section ready to receive entries
- **CONTRIBUTING.md** — local dev setup, branch strategy, commit convention, PR checklist
- **SECURITY.md** — disclosure contact (email or GitHub security advisory), supported versions
- **CODEOWNERS** — at least one owner per critical path

---

## Author

This template is maintained as part of the EPAS (Enterprise Platform Architecture Specification) work at `github.com/epas-platform/spec`.
