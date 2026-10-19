# 履约风险再校准复现材料 v0.3.0

本版对齐一次校准、持续更新及总评分变化，明确区分三层复现。未重新训练模型，也未在GitHub发布仓库。

## 公开汇总：一条命令生成核心表

推荐使用记录的Python 3.13复核环境（详见 docs/ENVIRONMENT_R2.json）：

```bash
python -m pip install -r requirements-review-lock.txt
python scripts/validate_revision.py
python scripts/rebuild_core_tables.py --out build/core
python scripts/make_revision_tables.py
python scripts/make_revision_figures.py
```

`rebuild_core_tables.py` 从已公开日级充分统计重新计算216行三项配对区间和96行跨主干效应差区间，检查96行未知结局范围，输出主表 `Table_core_comparisons.csv`。这不是原始订单到模型的独立复现。输出目录须新建或为空。

## 保存分数重放

```bash
python scripts/align_core_comparisons.py --e17-dir /path/to/extracted/E17 --out outputs/r2
python scripts/replay_e17_calibration.py --archive /path/to/private_E17_archive.zip --origin O2 --out outputs/replay_O2
```

第一条需要原E17目录中的逐订单预测、池、指标和区间文件，不拟合模型；它重建三项比较、模型间直接效应差、Frozen时间轨迹和额外订单界限。第二条从基础分数重新拟合校准器，不重训LR。本次第二条在O2通过12,209单/420条池日志验证，其他历史核验单独记录。私有逐单输入不随公开包分发。

## 原始数据入口与边界

保留 `scripts/reproduce_olist_primary.py`，要求用户自行获得原始Olist ZIP。该入口限于既有核心S1/LR流程；本轮未重新运行原始数据训练，也不声称覆盖所有E17主干和辅助数据。逐项范围见 `docs/REPRODUCTION_COVERAGE.csv`。

较早评估期订单在标签可见且合格后，可以进入后续更新。禁止的是当次使用未来才可见的结局，而非一概禁止评估期反馈。预测不得回写。名义随访按代理观察终点减审批时间计算，相同阈值集合不构成独立证据。

## 发布前

原始交易、逐单预测、模型和字体文件均不包含。发布者仍需审核衍生数据共享权限、填写作者引用信息并决定代码许可。`CITATION_TEMPLATE.cff` 尚不是已完成作者资料的正式引用文件。运行 `python scripts/audit_public_files.py` 并人工检查待提交文件；自动扫描不等于隐私/许可保证。建议仓库名 `fulfillment-recalibration-repro`。
