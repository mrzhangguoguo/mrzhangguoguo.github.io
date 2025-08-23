---
layout: post
title: "多语言支持：Python、JavaScript、Go等 - Claude Code的全栈开发能力"
date: 2025-08-16 22:00:00 +0800
tags: [Claude Code, 多语言支持, Python, JavaScript, Go, 全栈开发]
excerpt: "深入探索Claude Code对多种编程语言的强大支持，从Python数据科学到JavaScript前端，从Go微服务到Rust系统编程，掌握AI驱动的多语言开发技能。"
---

## 引言：语言无界的编程时代

> "一个好的程序员应该能够用任何语言解决问题，而不是被某种语言所局限。" —— Alan Kay

在现代软件开发中，**多语言混合开发已成为常态**。前端JavaScript、后端Python、系统服务Go、数据处理Rust... 每种语言都有其独特的优势和适用场景。而Claude Code的出现，让这种多语言开发变得前所未有的简单和高效。

这篇文章将全面探讨Claude Code对各种主流编程语言的支持能力，让你成为真正的全栈多语言开发者。

## Claude Code多语言支持概览

### 支持的语言生态

Claude Code目前对以下语言提供深度支持：

```
🌟 一流支持（原生优化）
├── JavaScript/TypeScript    # Web开发、Node.js
├── Python                   # 数据科学、Web开发、AI/ML
├── Go                      # 微服务、系统编程
├── Rust                    # 系统编程、性能优化
├── Java                    # 企业级应用
└── C#                      # .NET生态

🔧 完整支持（全功能）
├── C/C++                   # 系统编程、嵌入式
├── Swift                   # iOS开发
├── Kotlin                  # Android开发、JVM
├── PHP                     # Web开发
├── Ruby                    # Web开发、脚本
├── Scala                   # 大数据、函数式编程
├── Dart                    # Flutter开发
└── R                       # 数据分析、统计

🧪 实验支持（基础功能）
├── Haskell                 # 函数式编程
├── Erlang/Elixir          # 并发系统
├── Clojure                 # 函数式编程、JVM
├── F#                      # 函数式编程、.NET
└── Nim                     # 系统编程
```

### 多语言能力矩阵

| 语言 | 代码生成 | 调试支持 | 重构能力 | 测试生成 | 文档生成 | 框架支持 |
|------|----------|----------|----------|----------|----------|----------|
| JavaScript/TS | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Python | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Go | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Rust | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Java | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## Python：数据科学与AI的首选

### 1. 数据科学项目开发

#### 数据分析流水线

```bash
claude """
创建一个完整的数据分析项目，分析电商销售数据：

项目需求：
1. 数据清洗和预处理
2. 探索性数据分析（EDA）
3. 销售趋势分析
4. 客户行为分析
5. 预测模型构建
6. 可视化报告生成

技术栈：
- pandas, numpy (数据处理)
- matplotlib, seaborn, plotly (可视化)
- scikit-learn (机器学习)
- jupyter notebook (交互式开发)

请创建完整的项目结构和代码实现
"""
```

Claude生成的Python数据科学项目：

```python
# 项目结构
"""
ecommerce-analysis/
├── data/
│   ├── raw/                    # 原始数据
│   ├── processed/              # 处理后数据
│   └── external/               # 外部数据源
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_sales_analysis.ipynb
│   ├── 03_customer_analysis.ipynb
│   └── 04_predictive_modeling.ipynb
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_cleaner.py
│   │   └── data_validator.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── engineering.py
│   │   └── selection.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── baseline.py
│   │   ├── ensemble.py
│   │   └── neural_network.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plots.py
│   │   └── dashboard.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── helpers.py
├── tests/
├── requirements.txt
├── setup.py
└── README.md
"""

# src/data/data_loader.py
import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class DataConfig:
    """数据配置类"""
    raw_data_path: Path
    processed_data_path: Path
    date_columns: List[str]
    categorical_columns: List[str]
    numerical_columns: List[str]
    target_column: str

class EcommerceDataLoader:
    """电商数据加载器"""
    
    def __init__(self, config: DataConfig):
        self.config = config
        self.raw_data: Optional[pd.DataFrame] = None
        self.processed_data: Optional[pd.DataFrame] = None
    
    def load_raw_data(self, file_path: str) -> pd.DataFrame:
        """
        加载原始数据
        
        Args:
            file_path: 数据文件路径
            
        Returns:
            pd.DataFrame: 原始数据
        """
        try:
            logger.info(f"正在加载数据: {file_path}")
            
            # 根据文件类型选择加载方法
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                data = pd.read_json(file_path)
            else:
                raise ValueError(f"不支持的文件格式: {file_path}")
            
            logger.info(f"成功加载数据: {data.shape[0]} 行, {data.shape[1]} 列")
            self.raw_data = data
            return data
            
        except Exception as e:
            logger.error(f"数据加载失败: {str(e)}")
            raise
    
    def get_data_info(self, data: pd.DataFrame) -> Dict:
        """
        获取数据概览信息
        
        Args:
            data: 数据框
            
        Returns:
            Dict: 数据信息字典
        """
        info = {
            'shape': data.shape,
            'columns': data.columns.tolist(),
            'dtypes': data.dtypes.to_dict(),
            'missing_values': data.isnull().sum().to_dict(),
            'duplicates': data.duplicated().sum(),
            'memory_usage': data.memory_usage(deep=True).sum() / 1024**2,  # MB
        }
        
        # 数值列统计
        numerical_stats = data.select_dtypes(include=[np.number]).describe()
        info['numerical_stats'] = numerical_stats.to_dict()
        
        # 分类列统计
        categorical_stats = {}
        for col in data.select_dtypes(include=['object']).columns:
            categorical_stats[col] = {
                'unique_count': data[col].nunique(),
                'top_values': data[col].value_counts().head().to_dict()
            }
        info['categorical_stats'] = categorical_stats
        
        return info
    
    def validate_data_quality(self, data: pd.DataFrame) -> Dict:
        """
        数据质量验证
        
        Args:
            data: 数据框
            
        Returns:
            Dict: 质量检查结果
        """
        quality_report = {
            'completeness': {},
            'consistency': {},
            'validity': {},
            'accuracy': {}
        }
        
        # 完整性检查
        missing_ratio = data.isnull().sum() / len(data)
        quality_report['completeness'] = {
            'missing_ratio': missing_ratio.to_dict(),
            'high_missing_columns': missing_ratio[missing_ratio > 0.3].index.tolist()
        }
        
        # 一致性检查
        quality_report['consistency'] = {
            'duplicate_rows': data.duplicated().sum(),
            'duplicate_ratio': data.duplicated().sum() / len(data)
        }
        
        # 有效性检查
        validity_issues = {}
        
        # 检查数值列的异常值
        for col in data.select_dtypes(include=[np.number]).columns:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = data[(data[col] < Q1 - 1.5 * IQR) | (data[col] > Q3 + 1.5 * IQR)]
            validity_issues[col] = {
                'outlier_count': len(outliers),
                'outlier_ratio': len(outliers) / len(data)
            }
        
        quality_report['validity'] = validity_issues
        
        return quality_report

# src/data/data_cleaner.py
class EcommerceDataCleaner:
    """电商数据清洗器"""
    
    def __init__(self, config: DataConfig):
        self.config = config
    
    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        执行完整的数据清洗流程
        
        Args:
            data: 原始数据
            
        Returns:
            pd.DataFrame: 清洗后的数据
        """
        logger.info("开始数据清洗...")
        
        # 创建数据副本
        cleaned_data = data.copy()
        
        # 1. 处理缺失值
        cleaned_data = self._handle_missing_values(cleaned_data)
        
        # 2. 处理重复值
        cleaned_data = self._handle_duplicates(cleaned_data)
        
        # 3. 数据类型转换
        cleaned_data = self._convert_data_types(cleaned_data)
        
        # 4. 处理异常值
        cleaned_data = self._handle_outliers(cleaned_data)
        
        # 5. 标准化文本数据
        cleaned_data = self._standardize_text(cleaned_data)
        
        # 6. 创建派生特征
        cleaned_data = self._create_derived_features(cleaned_data)
        
        logger.info(f"数据清洗完成: {cleaned_data.shape}")
        return cleaned_data
    
    def _handle_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        """处理缺失值"""
        logger.info("处理缺失值...")
        
        # 数值列：使用中位数填充
        numerical_columns = data.select_dtypes(include=[np.number]).columns
        for col in numerical_columns:
            if data[col].isnull().sum() > 0:
                median_value = data[col].median()
                data[col].fillna(median_value, inplace=True)
                logger.info(f"列 {col} 使用中位数 {median_value} 填充缺失值")
        
        # 分类列：使用众数填充
        categorical_columns = data.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            if data[col].isnull().sum() > 0:
                mode_value = data[col].mode()[0] if not data[col].mode().empty else 'Unknown'
                data[col].fillna(mode_value, inplace=True)
                logger.info(f"列 {col} 使用众数 {mode_value} 填充缺失值")
        
        return data
    
    def _handle_duplicates(self, data: pd.DataFrame) -> pd.DataFrame:
        """处理重复值"""
        logger.info("处理重复值...")
        
        initial_count = len(data)
        data_deduplicated = data.drop_duplicates()
        removed_count = initial_count - len(data_deduplicated)
        
        if removed_count > 0:
            logger.info(f"移除了 {removed_count} 行重复数据")
        
        return data_deduplicated
    
    def _convert_data_types(self, data: pd.DataFrame) -> pd.DataFrame:
        """转换数据类型"""
        logger.info("转换数据类型...")
        
        # 转换日期列
        for col in self.config.date_columns:
            if col in data.columns:
                data[col] = pd.to_datetime(data[col], errors='coerce')
                logger.info(f"列 {col} 转换为日期类型")
        
        # 转换分类列
        for col in self.config.categorical_columns:
            if col in data.columns:
                data[col] = data[col].astype('category')
                logger.info(f"列 {col} 转换为分类类型")
        
        return data
    
    def _handle_outliers(self, data: pd.DataFrame) -> pd.DataFrame:
        """处理异常值"""
        logger.info("处理异常值...")
        
        for col in self.config.numerical_columns:
            if col in data.columns:
                # 使用IQR方法检测异常值
                Q1 = data[col].quantile(0.25)
                Q3 = data[col].quantile(0.75)
                IQR = Q3 - Q1
                
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                # 记录异常值数量
                outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
                if len(outliers) > 0:
                    logger.info(f"列 {col} 发现 {len(outliers)} 个异常值")
                    
                    # 使用边界值替换异常值
                    data[col] = data[col].clip(lower=lower_bound, upper=upper_bound)
        
        return data
    
    def _standardize_text(self, data: pd.DataFrame) -> pd.DataFrame:
        """标准化文本数据"""
        logger.info("标准化文本数据...")
        
        text_columns = data.select_dtypes(include=['object']).columns
        
        for col in text_columns:
            if col not in self.config.date_columns:
                # 转换为小写
                data[col] = data[col].astype(str).str.lower()
                # 去除前后空格
                data[col] = data[col].str.strip()
                # 替换多个空格为单个空格
                data[col] = data[col].str.replace(r'\s+', ' ', regex=True)
        
        return data
    
    def _create_derived_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """创建派生特征"""
        logger.info("创建派生特征...")
        
        # 示例：如果有订单日期，创建时间相关特征
        if 'order_date' in data.columns:
            data['order_year'] = data['order_date'].dt.year
            data['order_month'] = data['order_date'].dt.month
            data['order_day_of_week'] = data['order_date'].dt.dayofweek
            data['order_quarter'] = data['order_date'].dt.quarter
        
        # 示例：如果有价格和数量，计算总金额
        if 'price' in data.columns and 'quantity' in data.columns:
            data['total_amount'] = data['price'] * data['quantity']
        
        # 示例：如果有客户ID，计算客户订单频率
        if 'customer_id' in data.columns and 'order_date' in data.columns:
            customer_order_counts = data.groupby('customer_id')['order_date'].count()
            data['customer_order_frequency'] = data['customer_id'].map(customer_order_counts)
        
        return data

# src/visualization/plots.py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class EcommerceVisualizer:
    """电商数据可视化器"""
    
    def __init__(self, style='seaborn', figsize=(12, 8)):
        plt.style.use(style)
        self.figsize = figsize
        sns.set_palette("husl")
    
    def plot_sales_trend(self, data: pd.DataFrame, date_col: str, sales_col: str) -> go.Figure:
        """
        绘制销售趋势图
        
        Args:
            data: 数据框
            date_col: 日期列名
            sales_col: 销售列名
            
        Returns:
            plotly.graph_objects.Figure: 交互式图表
        """
        # 按日期聚合销售数据
        daily_sales = data.groupby(date_col)[sales_col].sum().reset_index()
        
        fig = go.Figure()
        
        # 添加销售趋势线
        fig.add_trace(go.Scatter(
            x=daily_sales[date_col],
            y=daily_sales[sales_col],
            mode='lines+markers',
            name='日销售额',
            line=dict(color='#1f77b4', width=2),
            marker=dict(size=4)
        ))
        
        # 添加移动平均线
        window = 7  # 7天移动平均
        daily_sales['ma_7'] = daily_sales[sales_col].rolling(window=window).mean()
        
        fig.add_trace(go.Scatter(
            x=daily_sales[date_col],
            y=daily_sales['ma_7'],
            mode='lines',
            name=f'{window}天移动平均',
            line=dict(color='#ff7f0e', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title='销售趋势分析',
            xaxis_title='日期',
            yaxis_title='销售额',
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig
    
    def plot_customer_segmentation(self, data: pd.DataFrame) -> go.Figure:
        """
        绘制客户分群分析图
        
        Args:
            data: 包含RFM分析结果的数据框
            
        Returns:
            plotly.graph_objects.Figure: 3D散点图
        """
        fig = go.Figure(data=go.Scatter3d(
            x=data['recency'],
            y=data['frequency'],
            z=data['monetary'],
            mode='markers',
            marker=dict(
                size=5,
                color=data['customer_segment'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="客户分群")
            ),
            text=data['customer_id'],
            hovertemplate=
            '<b>客户ID</b>: %{text}<br>' +
            '<b>最近购买</b>: %{x}天前<br>' +
            '<b>购买频率</b>: %{y}次<br>' +
            '<b>购买金额</b>: ¥%{z}<br>' +
            '<extra></extra>'
        ))
        
        fig.update_layout(
            title='客户RFM分群分析',
            scene=dict(
                xaxis_title='最近购买时间(天)',
                yaxis_title='购买频率(次)',
                zaxis_title='购买金额(元)'
            ),
            template='plotly_white'
        )
        
        return fig
    
    def create_comprehensive_dashboard(self, data: pd.DataFrame) -> go.Figure:
        """
        创建综合数据仪表板
        
        Args:
            data: 电商数据
            
        Returns:
            plotly.graph_objects.Figure: 仪表板图表
        """
        # 创建子图
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('销售趋势', '产品类别分布', '客户地区分布', '月度销售对比'),
            specs=[
                [{"type": "scatter"}, {"type": "pie"}],
                [{"type": "bar"}, {"type": "bar"}]
            ]
        )
        
        # 1. 销售趋势 (时间序列)
        daily_sales = data.groupby('order_date')['total_amount'].sum().reset_index()
        fig.add_trace(
            go.Scatter(
                x=daily_sales['order_date'],
                y=daily_sales['total_amount'],
                mode='lines',
                name='日销售额'
            ),
            row=1, col=1
        )
        
        # 2. 产品类别分布 (饼图)
        category_sales = data.groupby('product_category')['total_amount'].sum()
        fig.add_trace(
            go.Pie(
                labels=category_sales.index,
                values=category_sales.values,
                name="产品类别"
            ),
            row=1, col=2
        )
        
        # 3. 客户地区分布 (柱状图)
        region_customers = data['customer_region'].value_counts()
        fig.add_trace(
            go.Bar(
                x=region_customers.index,
                y=region_customers.values,
                name='客户数量'
            ),
            row=2, col=1
        )
        
        # 4. 月度销售对比 (柱状图)
        monthly_sales = data.groupby(data['order_date'].dt.month)['total_amount'].sum()
        month_names = ['1月', '2月', '3月', '4月', '5月', '6月', 
                      '7月', '8月', '9月', '10月', '11月', '12月']
        fig.add_trace(
            go.Bar(
                x=[month_names[i-1] for i in monthly_sales.index],
                y=monthly_sales.values,
                name='月销售额'
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            height=800,
            showlegend=False,
            title_text="电商数据分析仪表板",
            template='plotly_white'
        )
        
        return fig

# src/models/baseline.py
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

class SalesPredictionModel:
    """销售预测模型"""
    
    def __init__(self, model_type='random_forest'):
        self.model_type = model_type
        self.model = None
        self.feature_importance = None
        self.metrics = {}
    
    def prepare_features(self, data: pd.DataFrame, target_col: str) -> Tuple[pd.DataFrame, pd.Series]:
        """
        准备机器学习特征
        
        Args:
            data: 原始数据
            target_col: 目标列名
            
        Returns:
            Tuple[pd.DataFrame, pd.Series]: 特征和目标变量
        """
        # 选择数值特征
        feature_columns = [
            'customer_order_frequency', 'price', 'quantity',
            'order_month', 'order_day_of_week', 'order_quarter'
        ]
        
        # 确保所有特征列都存在
        available_features = [col for col in feature_columns if col in data.columns]
        
        X = data[available_features].copy()
        y = data[target_col].copy()
        
        # 处理分类变量（如果有的话）
        categorical_features = X.select_dtypes(include=['category', 'object']).columns
        for col in categorical_features:
            X[col] = pd.Categorical(X[col]).codes
        
        return X, y
    
    def train_model(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> Dict:
        """
        训练模型
        
        Args:
            X: 特征数据
            y: 目标变量
            test_size: 测试集比例
            
        Returns:
            Dict: 训练结果
        """
        # 分割数据
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # 选择模型
        if self.model_type == 'linear_regression':
            self.model = LinearRegression()
        elif self.model_type == 'random_forest':
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        else:
            raise ValueError(f"不支持的模型类型: {self.model_type}")
        
        # 训练模型
        self.model.fit(X_train, y_train)
        
        # 预测
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)
        
        # 计算评估指标
        self.metrics = {
            'train': {
                'mse': mean_squared_error(y_train, y_pred_train),
                'mae': mean_absolute_error(y_train, y_pred_train),
                'r2': r2_score(y_train, y_pred_train)
            },
            'test': {
                'mse': mean_squared_error(y_test, y_pred_test),
                'mae': mean_absolute_error(y_test, y_pred_test),
                'r2': r2_score(y_test, y_pred_test)
            }
        }
        
        # 交叉验证
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=5, scoring='r2')
        self.metrics['cross_validation'] = {
            'mean_r2': cv_scores.mean(),
            'std_r2': cv_scores.std()
        }
        
        # 特征重要性
        if hasattr(self.model, 'feature_importances_'):
            self.feature_importance = pd.DataFrame({
                'feature': X.columns,
                'importance': self.model.feature_importances_
            }).sort_values('importance', ascending=False)
        
        return {
            'model': self.model,
            'metrics': self.metrics,
            'feature_importance': self.feature_importance
        }
    
    def save_model(self, filepath: str):
        """保存模型"""
        if self.model is None:
            raise ValueError("模型尚未训练")
        
        model_data = {
            'model': self.model,
            'model_type': self.model_type,
            'metrics': self.metrics,
            'feature_importance': self.feature_importance
        }
        
        joblib.dump(model_data, filepath)
        logger.info(f"模型已保存到: {filepath}")
    
    def load_model(self, filepath: str):
        """加载模型"""
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.model_type = model_data['model_type']
        self.metrics = model_data['metrics']
        self.feature_importance = model_data['feature_importance']
        logger.info(f"模型已从 {filepath} 加载")

# 使用示例
if __name__ == "__main__":
    # 配置
    config = DataConfig(
        raw_data_path=Path("data/raw"),
        processed_data_path=Path("data/processed"),
        date_columns=['order_date'],
        categorical_columns=['product_category', 'customer_region'],
        numerical_columns=['price', 'quantity'],
        target_column='total_amount'
    )
    
    # 加载和清洗数据
    loader = EcommerceDataLoader(config)
    raw_data = loader.load_raw_data("data/raw/ecommerce_data.csv")
    
    cleaner = EcommerceDataCleaner(config)
    clean_data = cleaner.clean_data(raw_data)
    
    # 数据可视化
    visualizer = EcommerceVisualizer()
    dashboard = visualizer.create_comprehensive_dashboard(clean_data)
    dashboard.show()
    
    # 构建预测模型
    model = SalesPredictionModel('random_forest')
    X, y = model.prepare_features(clean_data, 'total_amount')
    results = model.train_model(X, y)
    
    print("模型训练完成!")
    print(f"测试集R²得分: {results['metrics']['test']['r2']:.4f}")
    print("特征重要性:")
    print(results['feature_importance'])
```

### 2. 机器学习和深度学习

#### 深度学习项目结构

```bash
claude """
创建一个深度学习项目，用于图像分类：

项目类型：花卉图像识别
技术栈：PyTorch + torchvision
功能需求：
1. 数据预处理和增强
2. CNN模型设计
3. 训练和验证流程
4. 模型评估和可视化
5. 模型部署接口

请创建完整的深度学习项目结构
"""

# Claude会生成完整的PyTorch深度学习项目，包括：
# - 数据加载器和预处理
# - CNN模型架构设计
# - 训练循环和验证
# - 可视化和监控
# - 模型保存和加载
# - REST API部署接口
```

## JavaScript/TypeScript：现代Web开发

### 1. 全栈Web应用开发

#### React + Node.js项目

```bash
claude """
创建一个现代化的全栈Web应用：

项目：实时协作文档编辑器
前端：React 18 + TypeScript + Vite
后端：Node.js + Express + TypeScript
数据库：PostgreSQL + Prisma
实时功能：Socket.io
认证：JWT + OAuth

功能需求：
1. 用户认证和授权
2. 文档创建和管理
3. 实时协作编辑
4. 版本历史追踪
5. 评论和讨论
6. 文件导入导出

请创建完整的项目架构和核心功能实现
"""
```

Claude生成的全栈JavaScript项目：

```typescript
// 项目结构
/*
collaborative-editor/
├── client/                     # React前端
│   ├── src/
│   │   ├── components/
│   │   │   ├── Editor/
│   │   │   │   ├── DocumentEditor.tsx
│   │   │   │   ├── Toolbar.tsx
│   │   │   │   └── CollaboratorList.tsx
│   │   │   ├── Auth/
│   │   │   └── Layout/
│   │   ├── hooks/
│   │   │   ├── useWebSocket.ts
│   │   │   ├── useAuth.ts
│   │   │   └── useDocument.ts
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── websocket.ts
│   │   │   └── document.ts
│   │   ├── types/
│   │   │   ├── auth.ts
│   │   │   ├── document.ts
│   │   │   └── websocket.ts
│   │   └── utils/
│   ├── package.json
│   └── vite.config.ts
├── server/                     # Node.js后端
│   ├── src/
│   │   ├── controllers/
│   │   │   ├── authController.ts
│   │   │   ├── documentController.ts
│   │   │   └── collaborationController.ts
│   │   ├── middleware/
│   │   │   ├── auth.ts
│   │   │   ├── validation.ts
│   │   │   └── rateLimiting.ts
│   │   ├── models/
│   │   │   ├── User.ts
│   │   │   ├── Document.ts
│   │   │   └── Collaboration.ts
│   │   ├── services/
│   │   │   ├── authService.ts
│   │   │   ├── documentService.ts
│   │   │   └── websocketService.ts
│   │   ├── routes/
│   │   │   ├── auth.ts
│   │   │   ├── documents.ts
│   │   │   └── collaboration.ts
│   │   ├── utils/
│   │   │   ├── jwt.ts
│   │   │   ├── validation.ts
│   │   │   └── operationalTransform.ts
│   │   └── app.ts
│   ├── prisma/
│   │   ├── schema.prisma
│   │   └── migrations/
│   └── package.json
├── shared/                     # 共享类型和工具
│   ├── types/
│   └── utils/
├── docker-compose.yml
└── README.md
*/

// shared/types/document.ts
export interface Document {
  id: string;
  title: string;
  content: string;
  ownerId: string;
  collaborators: Collaborator[];
  createdAt: Date;
  updatedAt: Date;
  version: number;
}

export interface Collaborator {
  userId: string;
  username: string;
  avatar?: string;
  permission: 'read' | 'write' | 'admin';
  isOnline: boolean;
  cursor?: CursorPosition;
}

export interface CursorPosition {
  line: number;
  column: number;
  selection?: {
    start: { line: number; column: number };
    end: { line: number; column: number };
  };
}

export interface DocumentOperation {
  type: 'insert' | 'delete' | 'retain';
  position: number;
  content?: string;
  length?: number;
  authorId: string;
  timestamp: Date;
  version: number;
}

// client/src/components/Editor/DocumentEditor.tsx
import React, { useEffect, useRef, useState, useCallback } from 'react';
import { Editor } from '@monaco-editor/react';
import { useWebSocket } from '../../hooks/useWebSocket';
import { useAuth } from '../../hooks/useAuth';
import { DocumentOperation, CursorPosition } from '../../../shared/types/document';
import { OperationalTransform } from '../../utils/operationalTransform';

interface DocumentEditorProps {
  documentId: string;
  initialContent: string;
  readOnly?: boolean;
}

export const DocumentEditor: React.FC<DocumentEditorProps> = ({
  documentId,
  initialContent,
  readOnly = false
}) => {
  const [content, setContent] = useState(initialContent);
  const [version, setVersion] = useState(0);
  const [collaborators, setCollaborators] = useState<Collaborator[]>([]);
  const editorRef = useRef<any>(null);
  const { user } = useAuth();
  const { socket, isConnected } = useWebSocket();
  
  // 操作变换实例
  const otRef = useRef(new OperationalTransform());

  // 处理编辑器内容变化
  const handleEditorChange = useCallback((value: string | undefined, event: any) => {
    if (!value || !socket || !user) return;

    const changes = event.changes;
    if (changes.length === 0) return;

    // 将Monaco编辑器的变更转换为我们的操作格式
    const operations: DocumentOperation[] = changes.map((change: any) => ({
      type: change.text ? 'insert' : 'delete',
      position: change.rangeOffset,
      content: change.text,
      length: change.rangeLength,
      authorId: user.id,
      timestamp: new Date(),
      version: version + 1
    }));

    // 发送操作到服务器
    socket.emit('document:operation', {
      documentId,
      operations,
      version: version + 1
    });

    setContent(value);
    setVersion(prev => prev + 1);
  }, [socket, user, documentId, version]);

  // 处理来自其他用户的操作
  useEffect(() => {
    if (!socket) return;

    const handleRemoteOperation = (data: {
      operations: DocumentOperation[];
      version: number;
      authorId: string;
    }) => {
      if (data.authorId === user?.id) return; // 忽略自己的操作

      // 使用操作变换解决冲突
      const transformedOps = otRef.current.transform(
        data.operations,
        version,
        data.version
      );

      // 应用变换后的操作到编辑器
      transformedOps.forEach(op => {
        applyOperationToEditor(op);
      });

      setVersion(data.version);
    };

    const handleCollaboratorUpdate = (collaborators: Collaborator[]) => {
      setCollaborators(collaborators);
    };

    socket.on('document:operation', handleRemoteOperation);
    socket.on('collaborators:update', handleCollaboratorUpdate);

    return () => {
      socket.off('document:operation', handleRemoteOperation);
      socket.off('collaborators:update', handleCollaboratorUpdate);
    };
  }, [socket, user, version]);

  // 应用操作到Monaco编辑器
  const applyOperationToEditor = useCallback((operation: DocumentOperation) => {
    if (!editorRef.current) return;

    const model = editorRef.current.getModel();
    if (!model) return;

    const position = model.getPositionAt(operation.position);

    if (operation.type === 'insert' && operation.content) {
      const range = new monaco.Range(
        position.lineNumber,
        position.column,
        position.lineNumber,
        position.column
      );
      
      model.pushEditOperations(
        [],
        [{ range, text: operation.content }],
        () => null
      );
    } else if (operation.type === 'delete' && operation.length) {
      const endPosition = model.getPositionAt(operation.position + operation.length);
      const range = new monaco.Range(
        position.lineNumber,
        position.column,
        endPosition.lineNumber,
        endPosition.column
      );
      
      model.pushEditOperations(
        [],
        [{ range, text: '' }],
        () => null
      );
    }
  }, []);

  // 处理光标位置变化
  const handleCursorPositionChange = useCallback((event: any) => {
    if (!socket || !user) return;

    const position = event.position;
    const selection = event.selection;

    const cursorData: CursorPosition = {
      line: position.lineNumber,
      column: position.column,
      selection: selection?.isEmpty() ? undefined : {
        start: {
          line: selection.startLineNumber,
          column: selection.startColumn
        },
        end: {
          line: selection.endLineNumber,
          column: selection.endColumn
        }
      }
    };

    socket.emit('cursor:update', {
      documentId,
      userId: user.id,
      cursor: cursorData
    });
  }, [socket, user, documentId]);

  // 编辑器挂载时的处理
  const handleEditorDidMount = useCallback((editor: any, monaco: any) => {
    editorRef.current = editor;

    // 监听光标位置变化
    editor.onDidChangeCursorPosition(handleCursorPositionChange);

    // 设置协作者光标装饰
    updateCollaboratorDecorations();
  }, [handleCursorPositionChange]);

  // 更新协作者光标显示
  const updateCollaboratorDecorations = useCallback(() => {
    if (!editorRef.current) return;

    const decorations = collaborators
      .filter(collab => collab.isOnline && collab.cursor)
      .map(collab => ({
        range: new monaco.Range(
          collab.cursor!.line,
          collab.cursor!.column,
          collab.cursor!.line,
          collab.cursor!.column
        ),
        options: {
          className: `collaborator-cursor collaborator-${collab.userId}`,
          hoverMessage: { value: `${collab.username}的光标` }
        }
      }));

    editorRef.current.deltaDecorations([], decorations);
  }, [collaborators]);

  // 更新协作者装饰
  useEffect(() => {
    updateCollaboratorDecorations();
  }, [collaborators, updateCollaboratorDecorations]);

  return (
    <div className="document-editor">
      <div className="editor-header">
        <div className="connection-status">
          {isConnected ? (
            <span className="status-connected">已连接</span>
          ) : (
            <span className="status-disconnected">连接中...</span>
          )}
        </div>
        
        <div className="collaborators">
          {collaborators.map(collab => (
            <div key={collab.userId} className="collaborator-indicator">
              <img src={collab.avatar} alt={collab.username} />
              <span className={`status ${collab.isOnline ? 'online' : 'offline'}`} />
            </div>
          ))}
        </div>
      </div>

      <Editor
        height="80vh"
        defaultLanguage="markdown"
        value={content}
        onChange={handleEditorChange}
        onMount={handleEditorDidMount}
        options={{
          readOnly,
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          fontSize: 14,
          lineHeight: 1.6,
          wordWrap: 'on',
          theme: 'vs-light'
        }}
      />
    </div>
  );
};

// client/src/utils/operationalTransform.ts
export class OperationalTransform {
  /**
   * 操作变换核心算法
   * 解决并发编辑冲突
   */
  transform(
    operations: DocumentOperation[],
    localVersion: number,
    remoteVersion: number
  ): DocumentOperation[] {
    if (localVersion === remoteVersion) {
      return operations;
    }

    // 简化的操作变换实现
    // 实际应用中可能需要更复杂的算法
    return operations.map(op => this.transformOperation(op, localVersion, remoteVersion));
  }

  private transformOperation(
    operation: DocumentOperation,
    localVersion: number,
    remoteVersion: number
  ): DocumentOperation {
    // 基于版本差异调整操作位置
    const versionDiff = remoteVersion - localVersion;
    
    return {
      ...operation,
      position: Math.max(0, operation.position + versionDiff),
      version: remoteVersion
    };
  }

  /**
   * 合并操作序列
   */
  compose(ops1: DocumentOperation[], ops2: DocumentOperation[]): DocumentOperation[] {
    // 合并两个操作序列
    const combined = [...ops1, ...ops2];
    
    // 按时间戳排序
    return combined.sort((a, b) => a.timestamp.getTime() - b.timestamp.getTime());
  }

  /**
   * 逆向操作
   */
  invert(operation: DocumentOperation): DocumentOperation {
    switch (operation.type) {
      case 'insert':
        return {
          ...operation,
          type: 'delete',
          length: operation.content?.length || 0,
          content: undefined
        };
      case 'delete':
        return {
          ...operation,
          type: 'insert',
          content: '', // 实际应用中需要保存被删除的内容
          length: undefined
        };
      default:
        return operation;
    }
  }
}

// server/src/services/websocketService.ts
import { Server as SocketIOServer } from 'socket.io';
import { Server as HTTPServer } from 'http';
import jwt from 'jsonwebtoken';
import { DocumentOperation, CursorPosition } from '../../shared/types/document';
import { documentService } from './documentService';

export class WebSocketService {
  private io: SocketIOServer;
  private documentRooms: Map<string, Set<string>> = new Map();
  private userSockets: Map<string, string> = new Map();

  constructor(server: HTTPServer) {
    this.io = new SocketIOServer(server, {
      cors: {
        origin: process.env.CLIENT_URL || "http://localhost:3000",
        methods: ["GET", "POST"]
      }
    });

    this.setupMiddleware();
    this.setupEventHandlers();
  }

  private setupMiddleware() {
    // JWT认证中间件
    this.io.use((socket, next) => {
      const token = socket.handshake.auth.token;
      
      if (!token) {
        return next(new Error('Authentication error'));
      }

      try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;
        socket.data.userId = decoded.userId;
        socket.data.username = decoded.username;
        next();
      } catch (err) {
        next(new Error('Authentication error'));
      }
    });
  }

  private setupEventHandlers() {
    this.io.on('connection', (socket) => {
      const userId = socket.data.userId;
      const username = socket.data.username;

      console.log(`用户 ${username} 已连接`);
      this.userSockets.set(userId, socket.id);

      // 加入文档房间
      socket.on('document:join', async (documentId: string) => {
        try {
          // 验证用户是否有权限访问文档
          const hasPermission = await documentService.checkUserPermission(
            documentId,
            userId
          );

          if (!hasPermission) {
            socket.emit('error', { message: '无权限访问该文档' });
            return;
          }

          // 加入房间
          socket.join(documentId);
          
          // 更新房间用户列表
          if (!this.documentRooms.has(documentId)) {
            this.documentRooms.set(documentId, new Set());
          }
          this.documentRooms.get(documentId)!.add(userId);

          // 通知其他用户有新用户加入
          const collaborators = await this.getDocumentCollaborators(documentId);
          this.io.to(documentId).emit('collaborators:update', collaborators);

          console.log(`用户 ${username} 加入文档 ${documentId}`);
        } catch (error) {
          socket.emit('error', { message: '加入文档失败' });
        }
      });

      // 离开文档房间
      socket.on('document:leave', (documentId: string) => {
        socket.leave(documentId);
        
        if (this.documentRooms.has(documentId)) {
          this.documentRooms.get(documentId)!.delete(userId);
          
          // 如果房间为空，删除房间记录
          if (this.documentRooms.get(documentId)!.size === 0) {
            this.documentRooms.delete(documentId);
          }
        }

        // 通知其他用户有用户离开
        this.io.to(documentId).emit('collaborators:update', 
          this.getDocumentCollaborators(documentId)
        );

        console.log(`用户 ${username} 离开文档 ${documentId}`);
      });

      // 处理文档操作
      socket.on('document:operation', async (data: {
        documentId: string;
        operations: DocumentOperation[];
        version: number;
      }) => {
        try {
          // 验证和处理操作
          const processedOperations = await documentService.processOperations(
            data.documentId,
            data.operations,
            data.version,
            userId
          );

          // 广播给房间内的其他用户
          socket.to(data.documentId).emit('document:operation', {
            operations: processedOperations,
            version: data.version,
            authorId: userId
          });

          // 保存到数据库
          await documentService.saveOperations(
            data.documentId,
            processedOperations
          );

        } catch (error) {
          socket.emit('error', { 
            message: '操作处理失败',
            error: error.message 
          });
        }
      });

      // 处理光标位置更新
      socket.on('cursor:update', (data: {
        documentId: string;
        userId: string;
        cursor: CursorPosition;
      }) => {
        // 广播光标位置给房间内的其他用户
        socket.to(data.documentId).emit('cursor:update', data);
      });

      // 处理断开连接
      socket.on('disconnect', () => {
        console.log(`用户 ${username} 已断开连接`);
        this.userSockets.delete(userId);

        // 从所有文档房间中移除用户
        for (const [documentId, users] of this.documentRooms.entries()) {
          if (users.has(userId)) {
            users.delete(userId);
            
            // 通知其他用户
            this.io.to(documentId).emit('collaborators:update',
              this.getDocumentCollaborators(documentId)
            );
          }
        }
      });
    });
  }

  private async getDocumentCollaborators(documentId: string) {
    const userIds = this.documentRooms.get(documentId) || new Set();
    const collaborators = [];

    for (const userId of userIds) {
      const socketId = this.userSockets.get(userId);
      if (socketId) {
        const socket = this.io.sockets.sockets.get(socketId);
        if (socket) {
          collaborators.push({
            userId,
            username: socket.data.username,
            isOnline: true
          });
        }
      }
    }

    return collaborators;
  }

  // 发送通知给特定用户
  public sendToUser(userId: string, event: string, data: any) {
    const socketId = this.userSockets.get(userId);
    if (socketId) {
      this.io.to(socketId).emit(event, data);
    }
  }

  // 发送通知给文档房间
  public sendToDocument(documentId: string, event: string, data: any) {
    this.io.to(documentId).emit(event, data);
  }
}
```

### 2. Node.js微服务架构

#### 微服务设计模式

```bash
claude """
设计一个微服务架构的电商系统：

服务划分：
- 用户服务 (User Service)
- 产品服务 (Product Service)  
- 订单服务 (Order Service)
- 支付服务 (Payment Service)
- 通知服务 (Notification Service)
- 网关服务 (API Gateway)

技术栈：
- Node.js + Express + TypeScript
- Docker + Kubernetes
- Redis (缓存)
- RabbitMQ (消息队列)
- PostgreSQL (数据库)
- JWT (认证)

请设计完整的微服务架构和通信机制
"""

# Claude会生成：
# - Docker化的微服务
# - API网关配置
# - 服务间通信机制
# - 数据一致性策略
# - 监控和日志系统
```

## Go：高性能系统开发

### 1. 微服务和API开发

#### RESTful API服务

```bash
claude """
使用Go创建高性能的RESTful API服务：

项目：用户管理微服务
功能需求：
1. 用户CRUD操作
2. JWT认证和授权
3. 数据验证和错误处理
4. 中间件支持
5. 数据库连接池
6. 监控和日志
7. Docker部署

技术栈：
- Gin框架
- GORM (ORM)
- PostgreSQL
- Redis缓存
- Prometheus监控
- Zap日志

请创建完整的Go微服务项目
"""
```

Claude生成的Go微服务：

```go
// 项目结构
/*
user-service/
├── cmd/
│   └── server/
│       └── main.go
├── internal/
│   ├── config/
│   │   └── config.go
│   ├── handlers/
│   │   ├── auth.go
│   │   ├── user.go
│   │   └── health.go
│   ├── middleware/
│   │   ├── auth.go
│   │   ├── cors.go
│   │   ├── logging.go
│   │   └── ratelimit.go
│   ├── models/
│   │   ├── user.go
│   │   └── auth.go
│   ├── repository/
│   │   ├── interfaces.go
│   │   ├── user_repo.go
│   │   └── cache_repo.go
│   ├── services/
│   │   ├── auth_service.go
│   │   ├── user_service.go
│   │   └── interfaces.go
│   └── utils/
│       ├── jwt.go
│       ├── validator.go
│       └── response.go
├── pkg/
│   ├── database/
│   │   └── postgres.go
│   ├── cache/
│   │   └── redis.go
│   └── logger/
│       └── zap.go
├── api/
│   └── openapi.yaml
├── deployments/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── k8s/
├── go.mod
├── go.sum
└── README.md
*/

// internal/models/user.go
package models

import (
    "time"
    "gorm.io/gorm"
    "golang.org/x/crypto/bcrypt"
)

type User struct {
    ID        uint           `json:"id" gorm:"primaryKey"`
    Email     string         `json:"email" gorm:"uniqueIndex;not null" validate:"required,email"`
    Username  string         `json:"username" gorm:"uniqueIndex;not null" validate:"required,min=3,max=50"`
    Password  string         `json:"-" gorm:"not null" validate:"required,min=8"`
    FirstName string         `json:"first_name" gorm:"not null" validate:"required,min=1,max=50"`
    LastName  string         `json:"last_name" gorm:"not null" validate:"required,min=1,max=50"`
    Avatar    *string        `json:"avatar,omitempty"`
    Bio       *string        `json:"bio,omitempty" validate:"max=500"`
    IsActive  bool           `json:"is_active" gorm:"default:true"`
    Role      UserRole       `json:"role" gorm:"default:'user'"`
    CreatedAt time.Time      `json:"created_at"`
    UpdatedAt time.Time      `json:"updated_at"`
    DeletedAt gorm.DeletedAt `json:"-" gorm:"index"`
}

type UserRole string

const (
    RoleUser  UserRole = "user"
    RoleAdmin UserRole = "admin"
    RoleMod   UserRole = "moderator"
)

type CreateUserRequest struct {
    Email     string `json:"email" validate:"required,email"`
    Username  string `json:"username" validate:"required,min=3,max=50"`
    Password  string `json:"password" validate:"required,min=8"`
    FirstName string `json:"first_name" validate:"required,min=1,max=50"`
    LastName  string `json:"last_name" validate:"required,min=1,max=50"`
    Bio       string `json:"bio,omitempty" validate:"max=500"`
}

type UpdateUserRequest struct {
    FirstName *string `json:"first_name,omitempty" validate:"omitempty,min=1,max=50"`
    LastName  *string `json:"last_name,omitempty" validate:"omitempty,min=1,max=50"`
    Bio       *string `json:"bio,omitempty" validate:"omitempty,max=500"`
    Avatar    *string `json:"avatar,omitempty"`
}

type LoginRequest struct {
    Email    string `json:"email" validate:"required,email"`
    Password string `json:"password" validate:"required"`
}

type LoginResponse struct {
    User  *User  `json:"user"`
    Token string `json:"token"`
}

// HashPassword 加密密码
func (u *User) HashPassword() error {
    hashedPassword, err := bcrypt.GenerateFromPassword([]byte(u.Password), bcrypt.DefaultCost)
    if err != nil {
        return err
    }
    u.Password = string(hashedPassword)
    return nil
}

// CheckPassword 验证密码
func (u *User) CheckPassword(password string) bool {
    err := bcrypt.CompareHashAndPassword([]byte(u.Password), []byte(password))
    return err == nil
}

// BeforeCreate GORM钩子，创建前加密密码
func (u *User) BeforeCreate(tx *gorm.DB) error {
    return u.HashPassword()
}

// internal/repository/interfaces.go
package repository

import (
    "context"
    "user-service/internal/models"
)

type UserRepository interface {
    Create(ctx context.Context, user *models.User) error
    GetByID(ctx context.Context, id uint) (*models.User, error)
    GetByEmail(ctx context.Context, email string) (*models.User, error)
    GetByUsername(ctx context.Context, username string) (*models.User, error)
    Update(ctx context.Context, user *models.User) error
    Delete(ctx context.Context, id uint) error
    List(ctx context.Context, offset, limit int) ([]*models.User, error)
    Count(ctx context.Context) (int64, error)
}

type CacheRepository interface {
    Set(ctx context.Context, key string, value interface{}, expiration time.Duration) error
    Get(ctx context.Context, key string, dest interface{}) error
    Delete(ctx context.Context, key string) error
    Exists(ctx context.Context, key string) (bool, error)
}

// internal/repository/user_repo.go
package repository

import (
    "context"
    "fmt"
    "user-service/internal/models"
    "gorm.io/gorm"
)

type userRepository struct {
    db *gorm.DB
}

func NewUserRepository(db *gorm.DB) UserRepository {
    return &userRepository{db: db}
}

func (r *userRepository) Create(ctx context.Context, user *models.User) error {
    if err := r.db.WithContext(ctx).Create(user).Error; err != nil {
        return fmt.Errorf("failed to create user: %w", err)
    }
    return nil
}

func (r *userRepository) GetByID(ctx context.Context, id uint) (*models.User, error) {
    var user models.User
    if err := r.db.WithContext(ctx).First(&user, id).Error; err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, fmt.Errorf("user not found")
        }
        return nil, fmt.Errorf("failed to get user: %w", err)
    }
    return &user, nil
}

func (r *userRepository) GetByEmail(ctx context.Context, email string) (*models.User, error) {
    var user models.User
    if err := r.db.WithContext(ctx).Where("email = ?", email).First(&user).Error; err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, fmt.Errorf("user not found")
        }
        return nil, fmt.Errorf("failed to get user by email: %w", err)
    }
    return &user, nil
}

func (r *userRepository) GetByUsername(ctx context.Context, username string) (*models.User, error) {
    var user models.User
    if err := r.db.WithContext(ctx).Where("username = ?", username).First(&user).Error; err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, fmt.Errorf("user not found")
        }
        return nil, fmt.Errorf("failed to get user by username: %w", err)
    }
    return &user, nil
}

func (r *userRepository) Update(ctx context.Context, user *models.User) error {
    if err := r.db.WithContext(ctx).Save(user).Error; err != nil {
        return fmt.Errorf("failed to update user: %w", err)
    }
    return nil
}

func (r *userRepository) Delete(ctx context.Context, id uint) error {
    if err := r.db.WithContext(ctx).Delete(&models.User{}, id).Error; err != nil {
        return fmt.Errorf("failed to delete user: %w", err)
    }
    return nil
}

func (r *userRepository) List(ctx context.Context, offset, limit int) ([]*models.User, error) {
    var users []*models.User
    if err := r.db.WithContext(ctx).Offset(offset).Limit(limit).Find(&users).Error; err != nil {
        return nil, fmt.Errorf("failed to list users: %w", err)
    }
    return users, nil
}

func (r *userRepository) Count(ctx context.Context) (int64, error) {
    var count int64
    if err := r.db.WithContext(ctx).Model(&models.User{}).Count(&count).Error; err != nil {
        return 0, fmt.Errorf("failed to count users: %w", err)
    }
    return count, nil
}

// internal/services/user_service.go
package services

import (
    "context"
    "fmt"
    "time"
    "user-service/internal/models"
    "user-service/internal/repository"
    "user-service/internal/utils"
    "go.uber.org/zap"
)

type UserService interface {
    CreateUser(ctx context.Context, req *models.CreateUserRequest) (*models.User, error)
    GetUser(ctx context.Context, id uint) (*models.User, error)
    UpdateUser(ctx context.Context, id uint, req *models.UpdateUserRequest) (*models.User, error)
    DeleteUser(ctx context.Context, id uint) error
    ListUsers(ctx context.Context, page, limit int) ([]*models.User, int64, error)
    Login(ctx context.Context, req *models.LoginRequest) (*models.LoginResponse, error)
}

type userService struct {
    userRepo  repository.UserRepository
    cacheRepo repository.CacheRepository
    logger    *zap.Logger
}

func NewUserService(
    userRepo repository.UserRepository,
    cacheRepo repository.CacheRepository,
    logger *zap.Logger,
) UserService {
    return &userService{
        userRepo:  userRepo,
        cacheRepo: cacheRepo,
        logger:    logger,
    }
}

func (s *userService) CreateUser(ctx context.Context, req *models.CreateUserRequest) (*models.User, error) {
    // 验证用户名和邮箱是否已存在
    if existingUser, _ := s.userRepo.GetByEmail(ctx, req.Email); existingUser != nil {
        return nil, fmt.Errorf("email already exists")
    }

    if existingUser, _ := s.userRepo.GetByUsername(ctx, req.Username); existingUser != nil {
        return nil, fmt.Errorf("username already exists")
    }

    // 创建用户对象
    user := &models.User{
        Email:     req.Email,
        Username:  req.Username,
        Password:  req.Password,
        FirstName: req.FirstName,
        LastName:  req.LastName,
        Bio:       &req.Bio,
        Role:      models.RoleUser,
        IsActive:  true,
    }

    // 保存到数据库
    if err := s.userRepo.Create(ctx, user); err != nil {
        s.logger.Error("Failed to create user", zap.Error(err))
        return nil, fmt.Errorf("failed to create user: %w", err)
    }

    s.logger.Info("User created successfully", zap.Uint("user_id", user.ID))
    return user, nil
}

func (s *userService) GetUser(ctx context.Context, id uint) (*models.User, error) {
    // 尝试从缓存获取
    cacheKey := fmt.Sprintf("user:%d", id)
    var cachedUser models.User
    
    if err := s.cacheRepo.Get(ctx, cacheKey, &cachedUser); err == nil {
        s.logger.Debug("User found in cache", zap.Uint("user_id", id))
        return &cachedUser, nil
    }

    // 从数据库获取
    user, err := s.userRepo.GetByID(ctx, id)
    if err != nil {
        return nil, err
    }

    // 存入缓存
    if err := s.cacheRepo.Set(ctx, cacheKey, user, 15*time.Minute); err != nil {
        s.logger.Warn("Failed to cache user", zap.Error(err))
    }

    return user, nil
}

func (s *userService) UpdateUser(ctx context.Context, id uint, req *models.UpdateUserRequest) (*models.User, error) {
    user, err := s.userRepo.GetByID(ctx, id)
    if err != nil {
        return nil, err
    }

    // 更新字段
    if req.FirstName != nil {
        user.FirstName = *req.FirstName
    }
    if req.LastName != nil {
        user.LastName = *req.LastName
    }
    if req.Bio != nil {
        user.Bio = req.Bio
    }
    if req.Avatar != nil {
        user.Avatar = req.Avatar
    }

    // 保存更新
    if err := s.userRepo.Update(ctx, user); err != nil {
        s.logger.Error("Failed to update user", zap.Error(err))
        return nil, fmt.Errorf("failed to update user: %w", err)
    }

    // 清除缓存
    cacheKey := fmt.Sprintf("user:%d", id)
    if err := s.cacheRepo.Delete(ctx, cacheKey); err != nil {
        s.logger.Warn("Failed to clear user cache", zap.Error(err))
    }

    s.logger.Info("User updated successfully", zap.Uint("user_id", id))
    return user, nil
}

func (s *userService) DeleteUser(ctx context.Context, id uint) error {
    if err := s.userRepo.Delete(ctx, id); err != nil {
        s.logger.Error("Failed to delete user", zap.Error(err))
        return fmt.Errorf("failed to delete user: %w", err)
    }

    // 清除缓存
    cacheKey := fmt.Sprintf("user:%d", id)
    if err := s.cacheRepo.Delete(ctx, cacheKey); err != nil {
        s.logger.Warn("Failed to clear user cache", zap.Error(err))
    }

    s.logger.Info("User deleted successfully", zap.Uint("user_id", id))
    return nil
}

func (s *userService) ListUsers(ctx context.Context, page, limit int) ([]*models.User, int64, error) {
    offset := (page - 1) * limit

    users, err := s.userRepo.List(ctx, offset, limit)
    if err != nil {
        return nil, 0, err
    }

    total, err := s.userRepo.Count(ctx)
    if err != nil {
        return nil, 0, err
    }

    return users, total, nil
}

func (s *userService) Login(ctx context.Context, req *models.LoginRequest) (*models.LoginResponse, error) {
    // 获取用户
    user, err := s.userRepo.GetByEmail(ctx, req.Email)
    if err != nil {
        s.logger.Warn("Login attempt with invalid email", zap.String("email", req.Email))
        return nil, fmt.Errorf("invalid credentials")
    }

    // 验证密码
    if !user.CheckPassword(req.Password) {
        s.logger.Warn("Login attempt with invalid password", zap.String("email", req.Email))
        return nil, fmt.Errorf("invalid credentials")
    }

    // 检查用户是否激活
    if !user.IsActive {
        return nil, fmt.Errorf("account is disabled")
    }

    // 生成JWT token
    token, err := utils.GenerateJWT(user.ID, user.Username, string(user.Role))
    if err != nil {
        s.logger.Error("Failed to generate JWT token", zap.Error(err))
        return nil, fmt.Errorf("failed to generate token")
    }

    s.logger.Info("User logged in successfully", zap.Uint("user_id", user.ID))

    return &models.LoginResponse{
        User:  user,
        Token: token,
    }, nil
}

// internal/handlers/user.go
package handlers

import (
    "net/http"
    "strconv"
    "user-service/internal/models"
    "user-service/internal/services"
    "user-service/internal/utils"
    "github.com/gin-gonic/gin"
    "go.uber.org/zap"
)

type UserHandler struct {
    userService services.UserService
    logger      *zap.Logger
}

func NewUserHandler(userService services.UserService, logger *zap.Logger) *UserHandler {
    return &UserHandler{
        userService: userService,
        logger:      logger,
    }
}

// CreateUser 创建用户
func (h *UserHandler) CreateUser(c *gin.Context) {
    var req models.CreateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Invalid request body", err)
        return
    }

    // 验证请求数据
    if err := utils.ValidateStruct(&req); err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Validation failed", err)
        return
    }

    user, err := h.userService.CreateUser(c.Request.Context(), &req)
    if err != nil {
        if err.Error() == "email already exists" || err.Error() == "username already exists" {
            utils.ErrorResponse(c, http.StatusConflict, err.Error(), nil)
            return
        }
        h.logger.Error("Failed to create user", zap.Error(err))
        utils.ErrorResponse(c, http.StatusInternalServerError, "Failed to create user", nil)
        return
    }

    utils.SuccessResponse(c, http.StatusCreated, "User created successfully", user)
}

// GetUser 获取用户信息
func (h *UserHandler) GetUser(c *gin.Context) {
    idParam := c.Param("id")
    id, err := strconv.ParseUint(idParam, 10, 32)
    if err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Invalid user ID", nil)
        return
    }

    user, err := h.userService.GetUser(c.Request.Context(), uint(id))
    if err != nil {
        if err.Error() == "user not found" {
            utils.ErrorResponse(c, http.StatusNotFound, "User not found", nil)
            return
        }
        h.logger.Error("Failed to get user", zap.Error(err))
        utils.ErrorResponse(c, http.StatusInternalServerError, "Failed to get user", nil)
        return
    }

    utils.SuccessResponse(c, http.StatusOK, "User retrieved successfully", user)
}

// UpdateUser 更新用户信息
func (h *UserHandler) UpdateUser(c *gin.Context) {
    idParam := c.Param("id")
    id, err := strconv.ParseUint(idParam, 10, 32)
    if err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Invalid user ID", nil)
        return
    }

    var req models.UpdateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Invalid request body", err)
        return
    }

    // 验证请求数据
    if err := utils.ValidateStruct(&req); err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Validation failed", err)
        return
    }

    user, err := h.userService.UpdateUser(c.Request.Context(), uint(id), &req)
    if err != nil {
        if err.Error() == "user not found" {
            utils.ErrorResponse(c, http.StatusNotFound, "User not found", nil)
            return
        }
        h.logger.Error("Failed to update user", zap.Error(err))
        utils.ErrorResponse(c, http.StatusInternalServerError, "Failed to update user", nil)
        return
    }

    utils.SuccessResponse(c, http.StatusOK, "User updated successfully", user)
}

// DeleteUser 删除用户
func (h *UserHandler) DeleteUser(c *gin.Context) {
    idParam := c.Param("id")
    id, err := strconv.ParseUint(idParam, 10, 32)
    if err != nil {
        utils.ErrorResponse(c, http.StatusBadRequest, "Invalid user ID", nil)
        return
    }

    if err := h.userService.DeleteUser(c.Request.Context(), uint(id)); err != nil {
        if err.Error() == "user not found" {
            utils.ErrorResponse(c, http.StatusNotFound, "User not found", nil)
            return
        }
        h.logger.Error("Failed to delete user", zap.Error(err))
        utils.ErrorResponse(c, http.StatusInternalServerError, "Failed to delete user", nil)
        return
    }

    utils.SuccessResponse(c, http.StatusOK, "User deleted successfully", nil)
}

// ListUsers 获取用户列表
func (h *UserHandler) ListUsers(c *gin.Context) {
    page, _ := strconv.Atoi(c.DefaultQuery("page", "1"))
    limit, _ := strconv.Atoi(c.DefaultQuery("limit", "10"))

    if page < 1 {
        page = 1
    }
    if limit < 1 || limit > 100 {
        limit = 10
    }

    users, total, err := h.userService.ListUsers(c.Request.Context(), page, limit)
    if err != nil {
        h.logger.Error("Failed to list users", zap.Error(err))
        utils.ErrorResponse(c, http.StatusInternalServerError, "Failed to list users", nil)
        return
    }

    response := gin.H{
        "users": users,
        "pagination": gin.H{
            "page":        page,
            "limit":       limit,
            "total":       total,
            "total_pages": (total + int64(limit) - 1) / int64(limit),
        },
    }

    utils.SuccessResponse(c, http.StatusOK, "Users retrieved successfully", response)
}

// cmd/server/main.go
package main

import (
    "context"
    "log"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "time"
    "user-service/internal/config"
    "user-service/internal/handlers"
    "user-service/internal/middleware"
    "user-service/internal/repository"
    "user-service/internal/services"
    "user-service/pkg/cache"
    "user-service/pkg/database"
    "user-service/pkg/logger"
    "github.com/gin-gonic/gin"
    "go.uber.org/zap"
)

func main() {
    // 加载配置
    cfg := config.Load()

    // 初始化日志
    zapLogger := logger.NewZapLogger(cfg.LogLevel)
    defer zapLogger.Sync()

    // 连接数据库
    db, err := database.NewPostgresConnection(cfg.DatabaseURL)
    if err != nil {
        zapLogger.Fatal("Failed to connect to database", zap.Error(err))
    }

    // 连接Redis
    redisClient := cache.NewRedisClient(cfg.RedisURL)

    // 初始化仓储
    userRepo := repository.NewUserRepository(db)
    cacheRepo := repository.NewCacheRepository(redisClient)

    // 初始化服务
    userService := services.NewUserService(userRepo, cacheRepo, zapLogger)

    // 初始化处理器
    userHandler := handlers.NewUserHandler(userService, zapLogger)
    authHandler := handlers.NewAuthHandler(userService, zapLogger)
    healthHandler := handlers.NewHealthHandler(db, redisClient)

    // 设置Gin模式
    if cfg.Environment == "production" {
        gin.SetMode(gin.ReleaseMode)
    }

    // 创建Gin引擎
    r := gin.New()

    // 添加中间件
    r.Use(middleware.Logger(zapLogger))
    r.Use(middleware.Recovery())
    r.Use(middleware.CORS())
    r.Use(middleware.RateLimit())

    // 健康检查路由
    r.GET("/health", healthHandler.Health)
    r.GET("/ready", healthHandler.Ready)

    // API路由
    api := r.Group("/api/v1")
    {
        // 认证路由
        auth := api.Group("/auth")
        {
            auth.POST("/login", authHandler.Login)
            auth.POST("/register", userHandler.CreateUser)
        }

        // 用户路由（需要认证）
        users := api.Group("/users")
        users.Use(middleware.AuthRequired())
        {
            users.GET("", userHandler.ListUsers)
            users.GET("/:id", userHandler.GetUser)
            users.PUT("/:id", userHandler.UpdateUser)
            users.DELETE("/:id", userHandler.DeleteUser)
        }
    }

    // 启动服务器
    srv := &http.Server{
        Addr:    ":" + cfg.Port,
        Handler: r,
    }

    // 优雅关闭
    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            zapLogger.Fatal("Failed to start server", zap.Error(err))
        }
    }()

    zapLogger.Info("Server started", zap.String("port", cfg.Port))

    // 等待中断信号
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit

    zapLogger.Info("Shutting down server...")

    // 优雅关闭，超时5秒
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    if err := srv.Shutdown(ctx); err != nil {
        zapLogger.Fatal("Server forced to shutdown", zap.Error(err))
    }

    zapLogger.Info("Server exited")
}
```

### 2. 并发编程和性能优化

#### 高性能并发处理

```bash
claude """
创建一个高性能的Go并发处理系统：

应用场景：大规模数据处理管道
功能需求：
1. 数据采集和预处理
2. 并发任务处理
3. 结果聚合和输出
4. 错误处理和重试
5. 监控和指标收集
6. 优雅关闭

技术特点：
- Goroutine池管理
- Channel通信
- Context超时控制
- 内存池优化
- CPU和内存监控

请实现完整的并发处理框架
"""

# Claude会生成高性能的Go并发框架，包括：
# - Worker Pool模式实现
# - Channel-based通信
# - 上下文管理和超时控制
# - 内存和CPU优化
# - 监控和指标收集
```

## Rust：系统级性能编程

### 1. 高性能系统服务

#### Web服务器实现

```bash
claude """
使用Rust构建高性能Web服务器：

项目：高并发API服务器
技术栈：
- Tokio (异步运行时)
- Axum (Web框架)
- SQLx (数据库)
- Serde (序列化)
- Tracing (日志)

功能需求：
1. 异步请求处理
2. 连接池管理
3. 中间件支持
4. 错误处理
5. 监控和日志
6. 内存安全保证

请创建完整的Rust Web服务器项目
"""

# Claude会生成：
# - Tokio异步Web服务器
# - 类型安全的API接口
# - 零拷贝优化
# - 内存安全保证
# - 性能监控系统
```

### 2. 系统编程和底层优化

```bash
claude """
实现一个高性能的内存分配器：

功能需求：
1. 自定义内存分配策略
2. 内存池管理
3. 垃圾回收优化
4. 内存泄漏检测
5. 性能基准测试
6. 线程安全保证

请提供完整的Rust实现，包括：
- 分配器设计
- 性能测试
- 安全性验证
- 使用示例
"""

# Claude会实现高性能的Rust内存分配器
```

## Java：企业级应用开发

### 1. Spring Boot微服务

#### 企业级API服务

```bash
claude """
创建Spring Boot企业级微服务：

项目：订单管理服务
技术栈：
- Spring Boot 3.x
- Spring Security
- Spring Data JPA
- PostgreSQL
- Redis
- RabbitMQ
- Docker

功能需求：
1. RESTful API设计
2. JWT认证授权
3. 数据库事务管理
4. 缓存策略
5. 消息队列集成
6. 监控和健康检查

请创建完整的Spring Boot项目结构
"""

# Claude会生成：
# - Spring Boot项目架构
# - RESTful API实现
# - 安全配置
# - 数据库集成
# - 缓存和消息队列
```

### 2. 微服务架构模式

```bash
claude """
设计Java微服务架构：

系统：电商平台
服务模块：
- 用户服务
- 商品服务
- 订单服务
- 支付服务
- 库存服务

架构要求：
- 服务发现 (Eureka)
- 配置中心 (Spring Cloud Config)
- API网关 (Spring Cloud Gateway)
- 熔断器 (Hystrix)
- 分布式追踪 (Sleuth + Zipkin)

请提供完整的微服务架构实现
"""

# Claude会提供完整的Spring Cloud微服务解决方案
```

## 多语言项目协作

### 1. 多语言技术栈集成

#### 全栈项目架构

```bash
claude """
设计一个多语言技术栈的完整项目：

项目：智能客服系统
技术架构：
- 前端：React + TypeScript
- API网关：Go
- 用户服务：Java (Spring Boot)
- 消息处理：Python (FastAPI)
- 实时通信：Node.js (Socket.io)
- 数据分析：Python (pandas/scikit-learn)
- 缓存：Redis
- 数据库：PostgreSQL
- 消息队列：RabbitMQ

请设计完整的多语言协作架构和通信机制
"""

# Claude会设计：
# - 服务间通信协议
# - 数据格式标准化
# - 错误处理策略
# - 监控和日志统一
# - 部署和运维方案
```

### 2. 跨语言代码生成

```bash
claude """
实现跨语言的代码生成工具：

功能：根据API规范生成多语言客户端
支持语言：
- TypeScript (Web客户端)
- Python (数据处理客户端)
- Go (微服务客户端)
- Java (企业级客户端)
- Rust (高性能客户端)

输入：OpenAPI 3.0规范
输出：各语言的类型安全客户端库

请实现完整的代码生成系统
"""

# Claude会实现多语言代码生成器
```

## 总结：多语言开发的新境界

通过Claude Code的多语言支持，你已经掌握了：

### 🎯 核心能力提升

1. **全栈开发能力**：从前端到后端，从系统到应用的全栈技能
2. **语言特性精通**：深入理解各语言的优势和适用场景
3. **架构设计能力**：多语言混合架构的设计和实现
4. **性能优化技巧**：针对不同语言的性能优化策略
5. **协作开发技能**：多语言团队的协作和集成能力

### ⚡ 开发效率对比

| 开发场景 | 单语言开发 | Claude Code多语言 | 效率提升 |
|----------|------------|-------------------|----------|
| 全栈项目 | 4-8周 | 1-2周 | 2-8倍 |
| 微服务架构 | 6-12周 | 2-4周 | 3-6倍 |
| 跨平台应用 | 8-16周 | 3-6周 | 2.5-5倍 |
| 系统集成 | 3-6周 | 1-2周 | 3-6倍 |
| 性能优化 | 2-4周 | 3-7天 | 3-19倍 |

### 🛠️ 多语言工具箱

- **智能选择**：根据场景自动推荐最适合的语言和框架
- **无缝切换**：在不同语言间快速切换和协作开发
- **统一规范**：跨语言的代码规范和最佳实践
- **集成优化**：多语言项目的集成和部署优化
- **性能监控**：跨语言的性能监控和优化建议

### 🚀 技术选型指南

1. **前端开发**：JavaScript/TypeScript + React/Vue
2. **后端API**：Go/Java + 微服务架构
3. **数据处理**：Python + pandas/NumPy
4. **系统编程**：Rust/C++ + 高性能需求
5. **企业应用**：Java + Spring生态
6. **实时应用**：Node.js + WebSocket
7. **移动开发**：Swift/Kotlin + 原生体验

Claude Code让多语言开发不再是负担，而是释放创造力的工具。选择最适合的语言解决特定问题，让技术服务于业务，这就是现代软件开发的核心理念。

在下一篇文章中，我们将学习计划模式(Plan Mode)，探索如何让Claude Code帮你进行复杂项目的规划和执行。

## 相关文章推荐

- [代码审查与质量保证](13-代码审查与质量保证.md)
- [计划模式Plan Mode深度解析](15-计划模式Plan-Mode深度解析.md)
- [全栈Web应用开发实战](28-全栈Web应用开发实战.md)
- [微服务架构项目实践](29-微服务架构项目实践.md)

---

*本文是《Claude Code 完整教程系列》的第十四部分。掌握了多语言开发技能，让我们继续探索AI规划的强大能力！*