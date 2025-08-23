---
layout: post
title: "全栈Web应用开发实战：Claude Code驱动的现代Web开发"
date: 2025-08-17 12:00:00 +0800
tags: [Claude Code, 全栈开发, Web应用, 现代前端, 后端开发, 实战项目]
excerpt: "深入探索使用Claude Code进行全栈Web应用开发的完整实践，从前端React到后端Node.js，从数据库设计到API开发，构建现代化、高性能的Web应用系统。"
---

## 引言：全栈开发的AI时代

> "The best way to predict the future is to invent it." —— Alan Kay

在现代Web开发中，**全栈开发已成为构建完整数字产品的核心技能**。而Claude Code的出现，为全栈开发带来了革命性的变化：AI不再只是辅助工具，而是成为了智能的开发伙伴，能够理解业务需求、生成高质量代码、优化架构设计。

传统的全栈开发面临诸多挑战：前后端技术栈的复杂性、API设计的一致性、数据库优化、部署配置、性能调优等。Claude Code通过AI驱动的开发模式，不仅能快速生成各层代码，更能确保架构的合理性和代码的质量。

这篇文章将带你完整实践一个现代全栈Web应用的开发过程，从需求分析到最终部署，体验AI增强的全栈开发威力。

## 项目规划和架构设计

### 实战项目：智能任务管理系统

```
项目概述 - TaskFlow AI
🎯 项目目标: 构建一个AI增强的任务管理平台
📋 核心功能:
  - 用户认证和权限管理
  - 智能任务创建和分类  
  - AI驱动的任务优先级推荐
  - 团队协作和实时同步
  - 数据可视化和报告
  - 移动端响应式设计

🏗️ 技术栈选择:
前端: React 18 + TypeScript + Tailwind CSS + Vite
后端: Node.js + Express + TypeScript + Prisma
数据库: PostgreSQL + Redis
AI服务: Claude API集成
部署: Docker + Nginx + PM2

🎨 设计理念:
  - 现代化UI/UX设计
  - 组件化和模块化架构
  - 类型安全的全栈开发
  - 高性能和可扩展性
  - 持续集成和部署
```

### 系统架构设计

```mermaid
graph TB
    A[用户界面 - React Frontend] --> B[API网关 - Express.js]
    B --> C[业务逻辑层 - Controllers]
    C --> D[服务层 - Services]
    D --> E[数据访问层 - Prisma ORM]
    E --> F[数据库 - PostgreSQL]
    
    D --> G[缓存层 - Redis]
    D --> H[AI服务 - Claude API]
    D --> I[文件存储 - AWS S3]
    
    J[WebSocket Server] --> A
    K[任务调度器 - Cron Jobs] --> D
    
    subgraph "外部服务"
        L[Claude AI API]
        M[邮件服务 - SendGrid]
        N[推送服务 - FCM]
    end
    
    H --> L
    D --> M
    D --> N
    
    subgraph "监控和日志"
        O[Prometheus + Grafana]
        P[Winston Logger]
        Q[Sentry错误监控]
    end
    
    B --> O
    C --> P
    A --> Q
```

## 前端开发实战

### 1. React项目初始化和配置

#### 使用Claude Code创建项目结构

```bash
# 使用Claude Code创建现代React项目
claude create react-app taskflow-frontend --template typescript

# 进入项目目录
cd taskflow-frontend

# 安装核心依赖
npm install @tanstack/react-query axios react-router-dom
npm install @headlessui/react @heroicons/react 
npm install react-hook-form @hookform/resolvers zod
npm install tailwindcss @tailwindcss/forms @tailwindcss/typography

# 安装开发依赖
npm install -D @types/react @types/react-dom
npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
npm install -D prettier eslint-plugin-prettier
npm install -D @testing-library/react @testing-library/jest-dom vitest
```

#### 现代化项目结构

```
src/
├── components/           # 可复用组件
│   ├── ui/              # 基础UI组件
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   │   └── Loading.tsx
│   ├── forms/           # 表单组件
│   │   ├── TaskForm.tsx
│   │   └── UserForm.tsx
│   └── layout/          # 布局组件
│       ├── Header.tsx
│       ├── Sidebar.tsx
│       └── Layout.tsx
├── pages/               # 页面组件
│   ├── auth/           # 认证相关页面
│   ├── dashboard/      # 仪表板
│   ├── tasks/          # 任务管理
│   └── profile/        # 用户资料
├── hooks/              # 自定义Hooks
│   ├── useAuth.ts
│   ├── useTasks.ts
│   └── useWebSocket.ts
├── services/           # API服务
│   ├── api.ts          # API客户端配置
│   ├── authService.ts  # 认证服务
│   └── taskService.ts  # 任务服务
├── store/              # 状态管理
│   ├── authStore.ts    # 认证状态
│   ├── taskStore.ts    # 任务状态
│   └── uiStore.ts      # UI状态
├── types/              # TypeScript类型定义
│   ├── auth.ts
│   ├── task.ts
│   └── api.ts
├── utils/              # 工具函数
│   ├── helpers.ts
│   ├── validators.ts
│   └── constants.ts
└── styles/             # 样式文件
    ├── globals.css
    └── components.css
```

### 2. 核心组件开发

#### 智能任务表单组件

```typescript
// src/components/forms/TaskForm.tsx
import React, { useState, useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Button } from '../ui/Button';
import { Input } from '../ui/Input';
import { Textarea } from '../ui/Textarea';
import { Select } from '../ui/Select';
import { useClaudeAI } from '../../hooks/useClaudeAI';
import { useTasks } from '../../hooks/useTasks';

// 任务表单验证Schema
const taskSchema = z.object({
  title: z.string().min(1, '任务标题不能为空').max(100, '标题过长'),
  description: z.string().optional(),
  priority: z.enum(['low', 'medium', 'high', 'urgent']),
  category: z.string().min(1, '请选择任务分类'),
  dueDate: z.string().optional(),
  assigneeId: z.string().optional(),
  tags: z.array(z.string()).default([])
});

type TaskFormData = z.infer<typeof taskSchema>;

interface TaskFormProps {
  initialData?: Partial<TaskFormData>;
  onSubmit: (data: TaskFormData) => void;
  onCancel: () => void;
  isLoading?: boolean;
}

export const TaskForm: React.FC<TaskFormProps> = ({
  initialData,
  onSubmit,
  onCancel,
  isLoading = false
}) => {
  const [aiSuggestions, setAiSuggestions] = useState<{
    priority?: string;
    category?: string;
    tags?: string[];
    estimatedTime?: string;
  }>({});
  
  const { generateTaskSuggestions } = useClaudeAI();
  const { categories, users } = useTasks();
  
  const {
    control,
    handleSubmit,
    watch,
    setValue,
    formState: { errors, isValid }
  } = useForm<TaskFormData>({
    resolver: zodResolver(taskSchema),
    defaultValues: {
      title: initialData?.title || '',
      description: initialData?.description || '',
      priority: initialData?.priority || 'medium',
      category: initialData?.category || '',
      dueDate: initialData?.dueDate || '',
      assigneeId: initialData?.assigneeId || '',
      tags: initialData?.tags || []
    }
  });
  
  const watchedTitle = watch('title');
  const watchedDescription = watch('description');
  
  // AI增强：基于标题和描述生成智能建议
  useEffect(() => {
    const generateAISuggestions = async () => {
      if (watchedTitle.length > 5) {
        try {
          const suggestions = await generateTaskSuggestions({
            title: watchedTitle,
            description: watchedDescription
          });
          
          setAiSuggestions(suggestions);
          
          // 自动应用AI建议（用户可以修改）
          if (suggestions.priority && !initialData?.priority) {
            setValue('priority', suggestions.priority as any);
          }
          
          if (suggestions.category && !initialData?.category) {
            setValue('category', suggestions.category);
          }
          
          if (suggestions.tags && suggestions.tags.length > 0) {
            setValue('tags', suggestions.tags);
          }
          
        } catch (error) {
          console.error('生成AI建议失败:', error);
        }
      }
    };
    
    const debounceTimer = setTimeout(generateAISuggestions, 1000);
    return () => clearTimeout(debounceTimer);
  }, [watchedTitle, watchedDescription, generateTaskSuggestions, setValue, initialData]);
  
  const handleFormSubmit = (data: TaskFormData) => {
    onSubmit(data);
  };
  
  const applyAISuggestion = (field: keyof TaskFormData, value: any) => {
    setValue(field, value);
  };
  
  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">
        {initialData ? '编辑任务' : '创建新任务'}
      </h2>
      
      <form onSubmit={handleSubmit(handleFormSubmit)} className="space-y-6">
        {/* 任务标题 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            任务标题 *
          </label>
          <Controller
            name="title"
            control={control}
            render={({ field }) => (
              <Input
                {...field}
                placeholder="输入任务标题..."
                error={errors.title?.message}
                className="w-full"
              />
            )}
          />
        </div>
        
        {/* 任务描述 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            任务描述
          </label>
          <Controller
            name="description"
            control={control}
            render={({ field }) => (
              <Textarea
                {...field}
                placeholder="详细描述任务内容..."
                rows={4}
                className="w-full"
              />
            )}
          />
        </div>
        
        {/* AI建议卡片 */}
        {Object.keys(aiSuggestions).length > 0 && (
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h3 className="text-sm font-medium text-blue-900 mb-3 flex items-center">
              <span className="mr-2">🤖</span>
              AI智能建议
            </h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {aiSuggestions.priority && (
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-700">
                    建议优先级: <strong>{aiSuggestions.priority}</strong>
                  </span>
                  <Button
                    type="button"
                    variant="outline"
                    size="sm"
                    onClick={() => applyAISuggestion('priority', aiSuggestions.priority)}
                  >
                    应用
                  </Button>
                </div>
              )}
              
              {aiSuggestions.category && (
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-700">
                    建议分类: <strong>{aiSuggestions.category}</strong>
                  </span>
                  <Button
                    type="button"
                    variant="outline"
                    size="sm"
                    onClick={() => applyAISuggestion('category', aiSuggestions.category)}
                  >
                    应用
                  </Button>
                </div>
              )}
              
              {aiSuggestions.tags && aiSuggestions.tags.length > 0 && (
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-700">
                    建议标签: <strong>{aiSuggestions.tags.join(', ')}</strong>
                  </span>
                  <Button
                    type="button"
                    variant="outline"
                    size="sm"
                    onClick={() => applyAISuggestion('tags', aiSuggestions.tags)}
                  >
                    应用
                  </Button>
                </div>
              )}
              
              {aiSuggestions.estimatedTime && (
                <div className="col-span-2">
                  <span className="text-sm text-gray-700">
                    预估完成时间: <strong>{aiSuggestions.estimatedTime}</strong>
                  </span>
                </div>
              )}
            </div>
          </div>
        )}
        
        {/* 表单字段网格 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* 优先级 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              优先级 *
            </label>
            <Controller
              name="priority"
              control={control}
              render={({ field }) => (
                <Select
                  {...field}
                  options={[
                    { value: 'low', label: '低优先级' },
                    { value: 'medium', label: '中优先级' },
                    { value: 'high', label: '高优先级' },
                    { value: 'urgent', label: '紧急' }
                  ]}
                  error={errors.priority?.message}
                />
              )}
            />
          </div>
          
          {/* 分类 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              任务分类 *
            </label>
            <Controller
              name="category"
              control={control}
              render={({ field }) => (
                <Select
                  {...field}
                  options={categories.map(cat => ({
                    value: cat.id,
                    label: cat.name
                  }))}
                  error={errors.category?.message}
                />
              )}
            />
          </div>
          
          {/* 截止日期 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              截止日期
            </label>
            <Controller
              name="dueDate"
              control={control}
              render={({ field }) => (
                <Input
                  {...field}
                  type="datetime-local"
                  className="w-full"
                />
              )}
            />
          </div>
          
          {/* 指派人员 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              指派给
            </label>
            <Controller
              name="assigneeId"
              control={control}
              render={({ field }) => (
                <Select
                  {...field}
                  options={[
                    { value: '', label: '未指派' },
                    ...users.map(user => ({
                      value: user.id,
                      label: user.name
                    }))
                  ]}
                />
              )}
            />
          </div>
        </div>
        
        {/* 标签 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            标签
          </label>
          <Controller
            name="tags"
            control={control}
            render={({ field }) => (
              <TagInput
                value={field.value}
                onChange={field.onChange}
                placeholder="添加标签..."
              />
            )}
          />
        </div>
        
        {/* 操作按钮 */}
        <div className="flex items-center justify-end space-x-4 pt-6 border-t">
          <Button
            type="button"
            variant="outline"
            onClick={onCancel}
            disabled={isLoading}
          >
            取消
          </Button>
          <Button
            type="submit"
            disabled={!isValid || isLoading}
            loading={isLoading}
          >
            {initialData ? '更新任务' : '创建任务'}
          </Button>
        </div>
      </form>
    </div>
  );
};

// 标签输入组件
const TagInput: React.FC<{
  value: string[];
  onChange: (tags: string[]) => void;
  placeholder?: string;
}> = ({ value, onChange, placeholder }) => {
  const [inputValue, setInputValue] = useState('');
  
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' || e.key === ',') {
      e.preventDefault();
      const newTag = inputValue.trim();
      if (newTag && !value.includes(newTag)) {
        onChange([...value, newTag]);
        setInputValue('');
      }
    }
  };
  
  const removeTag = (tagToRemove: string) => {
    onChange(value.filter(tag => tag !== tagToRemove));
  };
  
  return (
    <div className="border border-gray-300 rounded-md p-2 focus-within:ring-2 focus-within:ring-blue-500">
      <div className="flex flex-wrap gap-2 mb-2">
        {value.map((tag, index) => (
          <span
            key={index}
            className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
          >
            {tag}
            <button
              type="button"
              onClick={() => removeTag(tag)}
              className="ml-1 text-blue-600 hover:text-blue-800"
            >
              ×
            </button>
          </span>
        ))}
      </div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        className="w-full border-none outline-none text-sm"
      />
    </div>
  );
};
```

#### 智能仪表板组件

```typescript
// src/components/dashboard/Dashboard.tsx
import React, { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';
import { 
  CalendarIcon, 
  ClockIcon, 
  ChartBarIcon,
  UserIcon,
  ExclamationTriangleIcon,
  CheckCircleIcon
} from '@heroicons/react/24/outline';
import { useTasks } from '../../hooks/useTasks';
import { useAuth } from '../../hooks/useAuth';
import { useClaudeAI } from '../../hooks/useClaudeAI';
import { StatCard } from '../ui/StatCard';
import { TaskList } from './TaskList';
import { ProductivityChart } from './ProductivityChart';
import { AIInsights } from './AIInsights';

export const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const { 
    tasks, 
    getTaskStats, 
    getUpcomingTasks,
    getOverdueTasks,
    getCompletedTasksThisWeek 
  } = useTasks();
  const { generateProductivityInsights } = useClaudeAI();
  
  const [aiInsights, setAiInsights] = useState<any>(null);
  
  // 获取任务统计数据
  const { data: taskStats } = useQuery({
    queryKey: ['taskStats'],
    queryFn: getTaskStats
  });
  
  // 获取即将到期的任务
  const { data: upcomingTasks } = useQuery({
    queryKey: ['upcomingTasks'],
    queryFn: () => getUpcomingTasks(7) // 未来7天
  });
  
  // 获取逾期任务
  const { data: overdueTasks } = useQuery({
    queryKey: ['overdueTasks'],
    queryFn: getOverdueTasks
  });
  
  // 获取本周完成的任务
  const { data: completedTasks } = useQuery({
    queryKey: ['completedTasksThisWeek'],
    queryFn: getCompletedTasksThisWeek
  });
  
  // 生成AI生产力洞察
  useEffect(() => {
    const generateInsights = async () => {
      if (taskStats && completedTasks) {
        try {
          const insights = await generateProductivityInsights({
            taskStats,
            completedTasks,
            userWorkingHours: user?.preferences?.workingHours || '9-17'
          });
          setAiInsights(insights);
        } catch (error) {
          console.error('生成AI洞察失败:', error);
        }
      }
    };
    
    generateInsights();
  }, [taskStats, completedTasks, generateProductivityInsights, user]);
  
  if (!taskStats) {
    return <div className="flex justify-center items-center h-64">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>;
  }
  
  return (
    <div className="space-y-6">
      {/* 欢迎标题 */}
      <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg p-6 text-white">
        <h1 className="text-2xl font-bold mb-2">
          欢迎回来, {user?.name}！
        </h1>
        <p className="text-blue-100">
          今天是 {new Date().toLocaleDateString('zh-CN', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            weekday: 'long'
          })}
        </p>
      </div>
      
      {/* 统计卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard
          title="总任务数"
          value={taskStats.total}
          icon={<ChartBarIcon className="h-6 w-6" />}
          color="blue"
          trend={taskStats.totalTrend}
        />
        
        <StatCard
          title="待完成"
          value={taskStats.pending}
          icon={<ClockIcon className="h-6 w-6" />}
          color="yellow"
          trend={taskStats.pendingTrend}
        />
        
        <StatCard
          title="已完成"
          value={taskStats.completed}
          icon={<CheckCircleIcon className="h-6 w-6" />}
          color="green"
          trend={taskStats.completedTrend}
        />
        
        <StatCard
          title="逾期任务"
          value={overdueTasks?.length || 0}
          icon={<ExclamationTriangleIcon className="h-6 w-6" />}
          color="red"
          urgent={overdueTasks && overdueTasks.length > 0}
        />
      </div>
      
      {/* AI洞察 */}
      {aiInsights && (
        <AIInsights insights={aiInsights} />
      )}
      
      {/* 主要内容区域 */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* 即将到期的任务 */}
        <div className="lg:col-span-2">
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
              <CalendarIcon className="h-5 w-5 mr-2 text-gray-600" />
              即将到期的任务
            </h2>
            <TaskList 
              tasks={upcomingTasks || []}
              showStatus={false}
              showDueDate={true}
              compact={true}
            />
          </div>
        </div>
        
        {/* 生产力图表 */}
        <div>
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">
              本周生产力
            </h2>
            <ProductivityChart data={completedTasks} />
          </div>
        </div>
      </div>
      
      {/* 逾期任务提醒 */}
      {overdueTasks && overdueTasks.length > 0 && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-6">
          <h2 className="text-lg font-semibold text-red-900 mb-4 flex items-center">
            <ExclamationTriangleIcon className="h-5 w-5 mr-2" />
            逾期任务提醒
          </h2>
          <TaskList 
            tasks={overdueTasks}
            showStatus={true}
            showDueDate={true}
            variant="danger"
          />
        </div>
      )}
      
      {/* 最近活动 */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">
          最近活动
        </h2>
        <RecentActivity />
      </div>
    </div>
  );
};

// AI洞察组件
const AIInsights: React.FC<{ insights: any }> = ({ insights }) => {
  return (
    <div className="bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg p-6 border border-purple-200">
      <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
        <span className="mr-2">🤖</span>
        AI生产力洞察
      </h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {insights.recommendations?.map((rec: any, index: number) => (
          <div key={index} className="bg-white rounded-lg p-4 shadow-sm">
            <h3 className="font-medium text-gray-900 mb-2">{rec.title}</h3>
            <p className="text-sm text-gray-600 mb-3">{rec.description}</p>
            <div className="flex items-center justify-between">
              <span className="text-xs text-purple-600 font-medium">
                预期效果: {rec.expectedImpact}
              </span>
              <button className="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded">
                查看详情
              </button>
            </div>
          </div>
        ))}
      </div>
      
      {insights.productivity_score && (
        <div className="mt-4 p-4 bg-white rounded-lg">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium text-gray-700">
              本周生产力评分
            </span>
            <span className="text-2xl font-bold text-purple-600">
              {insights.productivity_score}/100
            </span>
          </div>
          <div className="mt-2 w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-gradient-to-r from-purple-500 to-blue-500 h-2 rounded-full"
              style={{ width: `${insights.productivity_score}%` }}
            ></div>
          </div>
        </div>
      )}
    </div>
  );
};

// 最近活动组件
const RecentActivity: React.FC = () => {
  const { data: activities } = useQuery({
    queryKey: ['recentActivities'],
    queryFn: () => fetch('/api/activities/recent').then(res => res.json())
  });
  
  if (!activities) return <div>加载中...</div>;
  
  return (
    <div className="space-y-4">
      {activities.map((activity: any) => (
        <div key={activity.id} className="flex items-center space-x-4 p-3 bg-gray-50 rounded-lg">
          <div className="flex-shrink-0">
            <UserIcon className="h-8 w-8 text-gray-400" />
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-sm text-gray-900">
              <span className="font-medium">{activity.user.name}</span>
              {' '}
              <span>{activity.action}</span>
              {' '}
              <span className="font-medium">{activity.task.title}</span>
            </p>
            <p className="text-xs text-gray-500">
              {new Date(activity.createdAt).toLocaleString('zh-CN')}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
};
```

### 3. 状态管理和API集成

#### React Query和状态管理

```typescript
// src/hooks/useTasks.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { toast } from 'react-hot-toast';
import { taskService } from '../services/taskService';
import { Task, CreateTaskData, UpdateTaskData, TaskFilters } from '../types/task';

export const useTasks = (filters?: TaskFilters) => {
  const queryClient = useQueryClient();
  
  // 获取任务列表
  const {
    data: tasks = [],
    isLoading,
    error,
    refetch
  } = useQuery({
    queryKey: ['tasks', filters],
    queryFn: () => taskService.getTasks(filters),
    staleTime: 5 * 60 * 1000, // 5分钟
  });
  
  // 创建任务
  const createTaskMutation = useMutation({
    mutationFn: (data: CreateTaskData) => taskService.createTask(data),
    onSuccess: (newTask) => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      queryClient.invalidateQueries({ queryKey: ['taskStats'] });
      toast.success('任务创建成功！');
    },
    onError: (error: any) => {
      toast.error(error.message || '创建任务失败');
    }
  });
  
  // 更新任务
  const updateTaskMutation = useMutation({
    mutationFn: ({ id, data }: { id: string; data: UpdateTaskData }) => 
      taskService.updateTask(id, data),
    onSuccess: (updatedTask) => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      queryClient.invalidateQueries({ queryKey: ['task', updatedTask.id] });
      toast.success('任务更新成功！');
    },
    onError: (error: any) => {
      toast.error(error.message || '更新任务失败');
    }
  });
  
  // 删除任务
  const deleteTaskMutation = useMutation({
    mutationFn: (id: string) => taskService.deleteTask(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      queryClient.invalidateQueries({ queryKey: ['taskStats'] });
      toast.success('任务删除成功！');
    },
    onError: (error: any) => {
      toast.error(error.message || '删除任务失败');
    }
  });
  
  // 完成任务
  const completeTaskMutation = useMutation({
    mutationFn: (id: string) => taskService.completeTask(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      queryClient.invalidateQueries({ queryKey: ['taskStats'] });
      toast.success('任务完成！');
    },
    onError: (error: any) => {
      toast.error(error.message || '完成任务失败');
    }
  });
  
  // 批量操作
  const batchUpdateMutation = useMutation({
    mutationFn: ({ ids, updates }: { ids: string[]; updates: Partial<Task> }) =>
      taskService.batchUpdate(ids, updates),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      toast.success('批量操作成功！');
    },
    onError: (error: any) => {
      toast.error(error.message || '批量操作失败');
    }
  });
  
  return {
    // 数据
    tasks,
    isLoading,
    error,
    
    // 操作
    createTask: createTaskMutation.mutate,
    updateTask: updateTaskMutation.mutate,
    deleteTask: deleteTaskMutation.mutate,
    completeTask: completeTaskMutation.mutate,
    batchUpdate: batchUpdateMutation.mutate,
    refetch,
    
    // 状态
    isCreating: createTaskMutation.isPending,
    isUpdating: updateTaskMutation.isPending,
    isDeleting: deleteTaskMutation.isPending,
    isCompleting: completeTaskMutation.isPending,
    isBatchUpdating: batchUpdateMutation.isPending,
    
    // 辅助方法
    getTaskById: (id: string) => tasks.find((task: Task) => task.id === id),
    getTasksByStatus: (status: string) => tasks.filter((task: Task) => task.status === status),
    getTasksByPriority: (priority: string) => tasks.filter((task: Task) => task.priority === priority),
  };
};

// Claude AI集成Hook
export const useClaudeAI = () => {
  const generateTaskSuggestions = async (taskData: {
    title: string;
    description?: string;
  }) => {
    try {
      const response = await fetch('/api/ai/task-suggestions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData)
      });
      
      if (!response.ok) {
        throw new Error('生成建议失败');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Claude AI API 错误:', error);
      throw error;
    }
  };
  
  const generateProductivityInsights = async (data: {
    taskStats: any;
    completedTasks: any[];
    userWorkingHours: string;
  }) => {
    try {
      const response = await fetch('/api/ai/productivity-insights', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
      
      if (!response.ok) {
        throw new Error('生成洞察失败');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Claude AI API 错误:', error);
      throw error;
    }
  };
  
  const optimizeTaskSchedule = async (tasks: Task[]) => {
    try {
      const response = await fetch('/api/ai/optimize-schedule', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tasks })
      });
      
      if (!response.ok) {
        throw new Error('优化排程失败');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Claude AI API 错误:', error);
      throw error;
    }
  };
  
  return {
    generateTaskSuggestions,
    generateProductivityInsights,
    optimizeTaskSchedule
  };
};
```

## 后端开发实战

### 1. Node.js项目结构和配置

#### Express + TypeScript + Prisma架构

```typescript
// src/app.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import compression from 'compression';
import { PrismaClient } from '@prisma/client';
import { createServer } from 'http';
import { Server as SocketServer } from 'socket.io';
import { authRouter } from './routes/auth';
import { taskRouter } from './routes/tasks';
import { userRouter } from './routes/users';
import { aiRouter } from './routes/ai';
import { errorHandler } from './middleware/errorHandler';
import { authMiddleware } from './middleware/auth';
import { loggerMiddleware } from './middleware/logger';
import { setupWebSocket } from './services/websocket';
import { setupCronJobs } from './services/scheduler';

// 初始化数据库客户端
export const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

// 创建Express应用
const app = express();
const server = createServer(app);
const io = new SocketServer(server, {
  cors: {
    origin: process.env.FRONTEND_URL || "http://localhost:3000",
    methods: ["GET", "POST"]
  }
});

// 基础中间件
app.use(helmet());
app.use(compression());
app.use(cors({
  origin: process.env.FRONTEND_URL || "http://localhost:3000",
  credentials: true
}));

// 速率限制
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15分钟
  max: 100, // 限制每个IP 15分钟内最多100个请求
  message: {
    error: '请求过于频繁，请稍后再试'
  }
});
app.use('/api/', limiter);

// 解析请求体
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// 日志中间件
app.use(loggerMiddleware);

// 健康检查
app.get('/health', (req, res) => {
  res.json({ 
    status: 'ok', 
    timestamp: new Date().toISOString(),
    version: process.env.APP_VERSION || '1.0.0'
  });
});

// API路由
app.use('/api/auth', authRouter);
app.use('/api/tasks', authMiddleware, taskRouter);
app.use('/api/users', authMiddleware, userRouter);
app.use('/api/ai', authMiddleware, aiRouter);

// 错误处理
app.use(errorHandler);

// 设置WebSocket
setupWebSocket(io);

// 设置定时任务
setupCronJobs();

// 优雅关闭
process.on('SIGTERM', async () => {
  console.log('SIGTERM received, shutting down gracefully');
  await prisma.$disconnect();
  server.close(() => {
    console.log('Process terminated');
  });
});

export { app, server, io };
```

#### 数据库模型设计 (Prisma Schema)

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String
  avatar    String?
  password  String
  role      Role     @default(USER)
  
  // 用户偏好设置
  preferences Json?
  
  // 时间戳
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  
  // 关系
  tasks         Task[]
  assignedTasks Task[] @relation("TaskAssignee")
  comments      Comment[]
  activities    Activity[]
  
  @@map("users")
}

model Task {
  id          String     @id @default(cuid())
  title       String
  description String?
  status      TaskStatus @default(TODO)
  priority    Priority   @default(MEDIUM)
  
  // 分类和标签
  category   Category @relation(fields: [categoryId], references: [id])
  categoryId String
  tags       Tag[]
  
  // 时间管理
  dueDate      DateTime?
  estimatedTime Int? // 预估时间（分钟）
  actualTime   Int? // 实际用时（分钟）
  startedAt    DateTime?
  completedAt  DateTime?
  
  // 用户关系
  creator   User   @relation(fields: [creatorId], references: [id])
  creatorId String
  assignee  User?  @relation("TaskAssignee", fields: [assigneeId], references: [id])
  assigneeId String?
  
  // AI增强字段
  aiSuggestions Json? // AI建议的内容
  complexityScore Float? // 复杂度评分
  
  // 时间戳
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  
  // 关系
  comments   Comment[]
  activities Activity[]
  subtasks   Task[]    @relation("SubTasks")
  parentTask Task?     @relation("SubTasks", fields: [parentId], references: [id])
  parentId   String?
  
  @@map("tasks")
}

model Category {
  id          String @id @default(cuid())
  name        String @unique
  description String?
  color       String @default("#3B82F6")
  
  // 时间戳
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  
  // 关系
  tasks Task[]
  
  @@map("categories")
}

model Tag {
  id    String @id @default(cuid())
  name  String @unique
  color String @default("#6B7280")
  
  // 时间戳
  createdAt DateTime @default(now())
  
  // 关系
  tasks Task[]
  
  @@map("tags")
}

model Comment {
  id      String @id @default(cuid())
  content String
  
  // 关系
  task   Task   @relation(fields: [taskId], references: [id], onDelete: Cascade)
  taskId String
  user   User   @relation(fields: [userId], references: [id])
  userId String
  
  // 时间戳
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  
  @@map("comments")
}

model Activity {
  id     String       @id @default(cuid())
  type   ActivityType
  action String
  
  // 元数据
  metadata Json?
  
  // 关系
  user   User   @relation(fields: [userId], references: [id])
  userId String
  task   Task?  @relation(fields: [taskId], references: [id])
  taskId String?
  
  // 时间戳
  createdAt DateTime @default(now())
  
  @@map("activities")
}

// 枚举类型
enum Role {
  USER
  ADMIN
  MANAGER
}

enum TaskStatus {
  TODO
  IN_PROGRESS
  IN_REVIEW
  COMPLETED
  CANCELLED
}

enum Priority {
  LOW
  MEDIUM
  HIGH
  URGENT
}

enum ActivityType {
  TASK_CREATED
  TASK_UPDATED
  TASK_COMPLETED
  TASK_DELETED
  COMMENT_ADDED
  USER_ASSIGNED
}
```

### 2. 核心业务逻辑实现

#### 任务服务层

```typescript
// src/services/taskService.ts
import { PrismaClient, Task, TaskStatus, Priority } from '@prisma/client';
import { ClaudeAIService } from './claudeAI';
import { NotificationService } from './notification';
import { ActivityService } from './activity';
import { CreateTaskData, UpdateTaskData, TaskFilters } from '../types/task';

export class TaskService {
  constructor(
    private prisma: PrismaClient,
    private claudeAI: ClaudeAIService,
    private notification: NotificationService,
    private activity: ActivityService
  ) {}
  
  async createTask(data: CreateTaskData, creatorId: string): Promise<Task> {
    try {
      // 使用Claude AI增强任务创建
      const aiEnhancements = await this.claudeAI.enhanceTaskCreation({
        title: data.title,
        description: data.description,
        category: data.categoryId
      });
      
      // 创建任务
      const task = await this.prisma.task.create({
        data: {
          ...data,
          creatorId,
          aiSuggestions: aiEnhancements,
          complexityScore: aiEnhancements.complexityScore,
          estimatedTime: aiEnhancements.estimatedTime
        },
        include: {
          creator: true,
          assignee: true,
          category: true,
          tags: true
        }
      });
      
      // 记录活动
      await this.activity.recordActivity({
        type: 'TASK_CREATED',
        action: '创建了任务',
        userId: creatorId,
        taskId: task.id,
        metadata: { taskTitle: task.title }
      });
      
      // 发送通知
      if (task.assigneeId && task.assigneeId !== creatorId) {
        await this.notification.sendTaskAssignedNotification(
          task.assigneeId,
          task
        );
      }
      
      return task;
    } catch (error) {
      throw new Error(`创建任务失败: ${error.message}`);
    }
  }
  
  async updateTask(
    id: string, 
    data: UpdateTaskData, 
    userId: string
  ): Promise<Task> {
    try {
      // 获取当前任务
      const currentTask = await this.prisma.task.findUnique({
        where: { id },
        include: { assignee: true }
      });
      
      if (!currentTask) {
        throw new Error('任务不存在');
      }
      
      // 检查权限
      const canUpdate = await this.checkUpdatePermission(currentTask, userId);
      if (!canUpdate) {
        throw new Error('没有权限更新此任务');
      }
      
      // AI智能更新建议
      let aiSuggestions = currentTask.aiSuggestions;
      if (data.title || data.description) {
        const suggestions = await this.claudeAI.getUpdateSuggestions({
          currentTask,
          updates: data
        });
        aiSuggestions = { ...aiSuggestions, ...suggestions };
      }
      
      // 更新任务
      const updatedTask = await this.prisma.task.update({
        where: { id },
        data: {
          ...data,
          aiSuggestions,
          updatedAt: new Date()
        },
        include: {
          creator: true,
          assignee: true,
          category: true,
          tags: true
        }
      });
      
      // 记录活动和发送通知
      await this.handleTaskUpdateEffects(currentTask, updatedTask, userId);
      
      return updatedTask;
    } catch (error) {
      throw new Error(`更新任务失败: ${error.message}`);
    }
  }
  
  async getTasks(filters: TaskFilters, userId: string): Promise<Task[]> {
    const whereClause: any = {
      OR: [
        { creatorId: userId },
        { assigneeId: userId }
      ]
    };
    
    // 应用过滤器
    if (filters.status) {
      whereClause.status = filters.status;
    }
    
    if (filters.priority) {
      whereClause.priority = filters.priority;
    }
    
    if (filters.categoryId) {
      whereClause.categoryId = filters.categoryId;
    }
    
    if (filters.search) {
      whereClause.OR = [
        { title: { contains: filters.search, mode: 'insensitive' } },
        { description: { contains: filters.search, mode: 'insensitive' } }
      ];
    }
    
    if (filters.dueDate) {
      whereClause.dueDate = {
        lte: new Date(filters.dueDate)
      };
    }
    
    return await this.prisma.task.findMany({
      where: whereClause,
      include: {
        creator: true,
        assignee: true,
        category: true,
        tags: true,
        _count: {
          select: {
            comments: true,
            subtasks: true
          }
        }
      },
      orderBy: [
        { priority: 'desc' },
        { dueDate: 'asc' },
        { createdAt: 'desc' }
      ]
    });
  }
  
  async completeTask(id: string, userId: string): Promise<Task> {
    try {
      const task = await this.prisma.task.findUnique({
        where: { id },
        include: { assignee: true, creator: true }
      });
      
      if (!task) {
        throw new Error('任务不存在');
      }
      
      // 检查权限
      const canComplete = task.assigneeId === userId || task.creatorId === userId;
      if (!canComplete) {
        throw new Error('没有权限完成此任务');
      }
      
      const completedTask = await this.prisma.task.update({
        where: { id },
        data: {
          status: TaskStatus.COMPLETED,
          completedAt: new Date(),
          actualTime: task.startedAt ? 
            Math.round((Date.now() - task.startedAt.getTime()) / 60000) : 
            undefined
        },
        include: {
          creator: true,
          assignee: true,
          category: true,
          tags: true
        }
      });
      
      // 记录活动
      await this.activity.recordActivity({
        type: 'TASK_COMPLETED',
        action: '完成了任务',
        userId,
        taskId: id,
        metadata: { 
          taskTitle: task.title,
          actualTime: completedTask.actualTime
        }
      });
      
      // AI分析完成效率
      await this.analyzeTaskCompletion(completedTask);
      
      // 发送完成通知
      if (task.creatorId !== userId) {
        await this.notification.sendTaskCompletedNotification(
          task.creatorId,
          completedTask
        );
      }
      
      return completedTask;
    } catch (error) {
      throw new Error(`完成任务失败: ${error.message}`);
    }
  }
  
  async getTaskStatistics(userId: string): Promise<any> {
    const stats = await this.prisma.task.groupBy({
      by: ['status'],
      where: {
        OR: [
          { creatorId: userId },
          { assigneeId: userId }
        ]
      },
      _count: {
        status: true
      }
    });
    
    const totalTasks = await this.prisma.task.count({
      where: {
        OR: [
          { creatorId: userId },
          { assigneeId: userId }
        ]
      }
    });
    
    const completedThisWeek = await this.prisma.task.count({
      where: {
        OR: [
          { creatorId: userId },
          { assigneeId: userId }
        ],
        status: TaskStatus.COMPLETED,
        completedAt: {
          gte: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)
        }
      }
    });
    
    const overdueTasks = await this.prisma.task.count({
      where: {
        OR: [
          { creatorId: userId },
          { assigneeId: userId }
        ],
        dueDate: {
          lt: new Date()
        },
        status: {
          not: TaskStatus.COMPLETED
        }
      }
    });
    
    return {
      total: totalTasks,
      byStatus: stats.reduce((acc, stat) => {
        acc[stat.status] = stat._count.status;
        return acc;
      }, {}),
      completedThisWeek,
      overdueTasks,
      completionRate: totalTasks > 0 ? 
        (stats.find(s => s.status === TaskStatus.COMPLETED)?._count.status || 0) / totalTasks * 100 : 
        0
    };
  }
  
  private async analyzeTaskCompletion(task: Task): Promise<void> {
    try {
      const analysis = await this.claudeAI.analyzeTaskCompletion({
        task,
        estimatedTime: task.estimatedTime,
        actualTime: task.actualTime
      });
      
      // 更新任务的AI分析结果
      await this.prisma.task.update({
        where: { id: task.id },
        data: {
          aiSuggestions: {
            ...task.aiSuggestions,
            completionAnalysis: analysis
          }
        }
      });
    } catch (error) {
      console.error('任务完成分析失败:', error);
    }
  }
  
  private async checkUpdatePermission(task: Task, userId: string): Promise<boolean> {
    // 任务创建者和被指派者都可以更新
    return task.creatorId === userId || task.assigneeId === userId;
  }
  
  private async handleTaskUpdateEffects(
    oldTask: Task,
    newTask: Task,
    userId: string
  ): Promise<void> {
    // 记录更新活动
    await this.activity.recordActivity({
      type: 'TASK_UPDATED',
      action: '更新了任务',
      userId,
      taskId: newTask.id,
      metadata: {
        changes: this.getTaskChanges(oldTask, newTask)
      }
    });
    
    // 如果指派人员发生变化，发送通知
    if (oldTask.assigneeId !== newTask.assigneeId) {
      if (newTask.assigneeId) {
        await this.notification.sendTaskAssignedNotification(
          newTask.assigneeId,
          newTask
        );
      }
      
      if (oldTask.assigneeId && oldTask.assigneeId !== userId) {
        await this.notification.sendTaskUnassignedNotification(
          oldTask.assigneeId,
          newTask
        );
      }
    }
    
    // 如果截止日期发生变化，发送提醒
    if (oldTask.dueDate !== newTask.dueDate && newTask.dueDate) {
      const daysUntilDue = Math.ceil(
        (newTask.dueDate.getTime() - Date.now()) / (1000 * 60 * 60 * 24)
      );
      
      if (daysUntilDue <= 3 && newTask.assigneeId) {
        await this.notification.sendDueDateReminderNotification(
          newTask.assigneeId,
          newTask,
          daysUntilDue
        );
      }
    }
  }
  
  private getTaskChanges(oldTask: Task, newTask: Task): any {
    const changes: any = {};
    
    if (oldTask.title !== newTask.title) {
      changes.title = { from: oldTask.title, to: newTask.title };
    }
    
    if (oldTask.status !== newTask.status) {
      changes.status = { from: oldTask.status, to: newTask.status };
    }
    
    if (oldTask.priority !== newTask.priority) {
      changes.priority = { from: oldTask.priority, to: newTask.priority };
    }
    
    if (oldTask.assigneeId !== newTask.assigneeId) {
      changes.assignee = { from: oldTask.assigneeId, to: newTask.assigneeId };
    }
    
    return changes;
  }
}
```

#### Claude AI服务集成

```typescript
// src/services/claudeAI.ts
import Anthropic from '@anthropic-ai/sdk';
import { Task, Category } from '@prisma/client';

export class ClaudeAIService {
  private claude: Anthropic;
  
  constructor() {
    this.claude = new Anthropic({
      apiKey: process.env.CLAUDE_API_KEY!,
    });
  }
  
  async enhanceTaskCreation(data: {
    title: string;
    description?: string;
    category?: string;
  }): Promise<any> {
    try {
      const prompt = this.buildTaskEnhancementPrompt(data);
      
      const response = await this.claude.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1000,
        messages: [{
          role: 'user',
          content: prompt
        }]
      });
      
      const content = response.content[0];
      if (content.type === 'text') {
        return JSON.parse(content.text);
      }
      
      return {};
    } catch (error) {
      console.error('Claude AI任务增强失败:', error);
      return {};
    }
  }
  
  async generateTaskSuggestions(data: {
    title: string;
    description?: string;
  }): Promise<any> {
    try {
      const prompt = `
作为一个智能任务管理助手，请分析以下任务信息并提供建议：

任务标题: ${data.title}
任务描述: ${data.description || '无'}

请以JSON格式返回以下建议：
{
  "priority": "建议的优先级 (low/medium/high/urgent)",
  "category": "建议的分类",
  "tags": ["建议的标签1", "建议的标签2"],
  "estimatedTime": "预估完成时间（分钟）",
  "complexity": "复杂度评分 (1-10)",
  "suggestions": [
    "改进建议1",
    "改进建议2"
  ],
  "breakdown": [
    "子任务1",
    "子任务2"
  ]
}

请基于任务的内容和复杂度给出合理建议。
`;
      
      const response = await this.claude.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1000,
        messages: [{
          role: 'user',
          content: prompt
        }]
      });
      
      const content = response.content[0];
      if (content.type === 'text') {
        return JSON.parse(content.text);
      }
      
      return {};
    } catch (error) {
      console.error('Claude AI建议生成失败:', error);
      return {};
    }
  }
  
  async generateProductivityInsights(data: {
    taskStats: any;
    completedTasks: Task[];
    userWorkingHours: string;
  }): Promise<any> {
    try {
      const prompt = `
作为生产力分析专家，请分析以下用户数据并提供洞察：

任务统计:
- 总任务数: ${data.taskStats.total}
- 已完成: ${data.taskStats.completed}
- 进行中: ${data.taskStats.inProgress}
- 完成率: ${data.taskStats.completionRate}%

最近完成的任务数量: ${data.completedTasks.length}
工作时间: ${data.userWorkingHours}

请以JSON格式返回分析结果：
{
  "productivity_score": "生产力评分 (0-100)",
  "trends": {
    "completion_trend": "完成趋势分析",
    "efficiency_trend": "效率趋势分析"
  },
  "recommendations": [
    {
      "title": "建议标题",
      "description": "具体建议",
      "expectedImpact": "预期效果",
      "priority": "优先级 (high/medium/low)"
    }
  ],
  "insights": [
    "关键洞察1",
    "关键洞察2"
  ],
  "next_week_forecast": {
    "predicted_completion": "预测下周完成任务数",
    "focus_areas": ["重点关注领域1", "重点关注领域2"]
  }
}

请提供实用的、个性化的建议。
`;
      
      const response = await this.claude.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1500,
        messages: [{
          role: 'user',
          content: prompt
        }]
      });
      
      const content = response.content[0];
      if (content.type === 'text') {
        return JSON.parse(content.text);
      }
      
      return {};
    } catch (error) {
      console.error('Claude AI生产力洞察生成失败:', error);
      return {};
    }
  }
  
  async optimizeTaskSchedule(tasks: Task[]): Promise<any> {
    try {
      const taskData = tasks.map(task => ({
        id: task.id,
        title: task.title,
        priority: task.priority,
        estimatedTime: task.estimatedTime,
        dueDate: task.dueDate,
        complexity: task.complexityScore
      }));
      
      const prompt = `
作为任务调度优化专家，请为以下任务列表制定最优的执行计划：

任务列表: ${JSON.stringify(taskData, null, 2)}

请考虑以下因素：
1. 任务优先级
2. 截止日期
3. 预估时间
4. 任务复杂度
5. 工作效率最优时间段

请以JSON格式返回优化后的排程：
{
  "optimized_schedule": [
    {
      "task_id": "任务ID",
      "recommended_start": "建议开始时间",
      "recommended_duration": "建议执行时长",
      "reasoning": "排程理由"
    }
  ],
  "schedule_insights": [
    "排程洞察1",
    "排程洞察2"
  ],
  "productivity_tips": [
    "生产力建议1",
    "生产力建议2"
  ]
}
`;
      
      const response = await this.claude.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 2000,
        messages: [{
          role: 'user',
          content: prompt
        }]
      });
      
      const content = response.content[0];
      if (content.type === 'text') {
        return JSON.parse(content.text);
      }
      
      return {};
    } catch (error) {
      console.error('Claude AI任务调度优化失败:', error);
      return {};
    }
  }
  
  async analyzeTaskCompletion(data: {
    task: Task;
    estimatedTime?: number;
    actualTime?: number;
  }): Promise<any> {
    try {
      const prompt = `
请分析以下任务完成情况：

任务信息:
- 标题: ${data.task.title}
- 预估时间: ${data.estimatedTime || '未设置'} 分钟
- 实际用时: ${data.actualTime || '未记录'} 分钟
- 优先级: ${data.task.priority}
- 复杂度: ${data.task.complexityScore || '未评估'}

请提供分析结果：
{
  "efficiency_score": "效率评分 (0-100)",
  "time_accuracy": "时间预估准确度",
  "performance_feedback": "表现反馈",
  "improvement_suggestions": [
    "改进建议1",
    "改进建议2"
  ],
  "learning_insights": [
    "学习洞察1",
    "学习洞察2"
  ]
}
`;
      
      const response = await this.claude.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1000,
        messages: [{
          role: 'user',
          content: prompt
        }]
      });
      
      const content = response.content[0];
      if (content.type === 'text') {
        return JSON.parse(content.text);
      }
      
      return {};
    } catch (error) {
      console.error('Claude AI任务完成分析失败:', error);
      return {};
    }
  }
  
  private buildTaskEnhancementPrompt(data: any): string {
    return `
作为智能任务管理系统，请分析并增强以下任务：

任务标题: ${data.title}
任务描述: ${data.description || '无'}
分类: ${data.category || '未分类'}

请返回JSON格式的增强信息：
{
  "priority": "建议优先级",
  "estimatedTime": 预估时间（分钟）,
  "complexityScore": 复杂度评分（1-10）,
  "tags": ["相关标签"],
  "breakdown": ["子任务分解"],
  "dependencies": ["可能的依赖"],
  "resources": ["需要的资源"],
  "risks": ["潜在风险"],
  "success_criteria": ["成功标准"]
}
`;
  }
}
```

## 实时功能和WebSocket

### WebSocket实时协作

```typescript
// src/services/websocket.ts
import { Server as SocketServer } from 'socket.io';
import { verifyJWT } from '../utils/jwt';
import { prisma } from '../app';

interface AuthenticatedSocket extends Socket {
  userId?: string;
}

export function setupWebSocket(io: SocketServer) {
  // 身份验证中间件
  io.use(async (socket: AuthenticatedSocket, next) => {
    try {
      const token = socket.handshake.auth.token;
      if (!token) {
        return next(new Error('未提供认证令牌'));
      }
      
      const decoded = verifyJWT(token);
      socket.userId = decoded.userId;
      next();
    } catch (error) {
      next(new Error('认证失败'));
    }
  });
  
  io.on('connection', (socket: AuthenticatedSocket) => {
    console.log(`用户 ${socket.userId} 已连接`);
    
    // 加入用户房间
    socket.join(`user:${socket.userId}`);
    
    // 任务相关事件
    setupTaskEvents(socket, io);
    
    // 协作编辑事件
    setupCollaborationEvents(socket, io);
    
    // 通知事件
    setupNotificationEvents(socket, io);
    
    socket.on('disconnect', () => {
      console.log(`用户 ${socket.userId} 已断开连接`);
    });
  });
}

function setupTaskEvents(socket: AuthenticatedSocket, io: SocketServer) {
  // 加入任务房间
  socket.on('join-task', (taskId: string) => {
    socket.join(`task:${taskId}`);
    
    // 通知其他用户有人加入了任务
    socket.to(`task:${taskId}`).emit('user-joined-task', {
      userId: socket.userId,
      taskId
    });
  });
  
  // 离开任务房间
  socket.on('leave-task', (taskId: string) => {
    socket.leave(`task:${taskId}`);
    
    // 通知其他用户有人离开了任务
    socket.to(`task:${taskId}`).emit('user-left-task', {
      userId: socket.userId,
      taskId
    });
  });
  
  // 任务状态更新
  socket.on('task-status-update', async (data: {
    taskId: string;
    status: string;
    comment?: string;
  }) => {
    try {
      // 更新数据库
      const task = await prisma.task.update({
        where: { id: data.taskId },
        data: { status: data.status as any },
        include: {
          creator: true,
          assignee: true
        }
      });
      
      // 广播给所有在任务房间的用户
      io.to(`task:${data.taskId}`).emit('task-updated', {
        task,
        updatedBy: socket.userId,
        changes: { status: data.status },
        comment: data.comment
      });
      
      // 发送给任务相关的用户
      if (task.assigneeId && task.assigneeId !== socket.userId) {
        io.to(`user:${task.assigneeId}`).emit('task-notification', {
          type: 'status-changed',
          task,
          message: `任务 "${task.title}" 状态已更新为 ${data.status}`
        });
      }
      
    } catch (error) {
      socket.emit('error', { message: '更新任务状态失败' });
    }
  });
  
  // 实时评论
  socket.on('add-comment', async (data: {
    taskId: string;
    content: string;
  }) => {
    try {
      const comment = await prisma.comment.create({
        data: {
          content: data.content,
          taskId: data.taskId,
          userId: socket.userId!
        },
        include: {
          user: true
        }
      });
      
      // 广播新评论
      io.to(`task:${data.taskId}`).emit('new-comment', comment);
      
    } catch (error) {
      socket.emit('error', { message: '添加评论失败' });
    }
  });
}

function setupCollaborationEvents(socket: AuthenticatedSocket, io: SocketServer) {
  // 用户正在编辑任务
  socket.on('start-editing', (data: {
    taskId: string;
    field: string;
  }) => {
    socket.to(`task:${data.taskId}`).emit('user-editing', {
      userId: socket.userId,
      taskId: data.taskId,
      field: data.field
    });
  });
  
  // 用户停止编辑
  socket.on('stop-editing', (data: {
    taskId: string;
    field: string;
  }) => {
    socket.to(`task:${data.taskId}`).emit('user-stopped-editing', {
      userId: socket.userId,
      taskId: data.taskId,
      field: data.field
    });
  });
  
  // 实时文本同步 (协作编辑)
  socket.on('text-change', (data: {
    taskId: string;
    field: string;
    content: string;
    cursor: number;
  }) => {
    socket.to(`task:${data.taskId}`).emit('text-updated', {
      userId: socket.userId,
      ...data
    });
  });
}

function setupNotificationEvents(socket: AuthenticatedSocket, io: SocketServer) {
  // 标记通知为已读
  socket.on('mark-notification-read', async (notificationId: string) => {
    try {
      await prisma.notification.update({
        where: { id: notificationId },
        data: { isRead: true }
      });
      
      socket.emit('notification-marked-read', { notificationId });
    } catch (error) {
      socket.emit('error', { message: '标记通知失败' });
    }
  });
  
  // 获取未读通知数量
  socket.on('get-unread-count', async () => {
    try {
      const count = await prisma.notification.count({
        where: {
          userId: socket.userId,
          isRead: false
        }
      });
      
      socket.emit('unread-count', { count });
    } catch (error) {
      socket.emit('error', { message: '获取未读通知数量失败' });
    }
  });
}

// 发送实时通知的辅助函数
export async function sendRealTimeNotification(
  io: SocketServer,
  userId: string,
  notification: any
) {
  io.to(`user:${userId}`).emit('new-notification', notification);
}

// 广播任务更新
export async function broadcastTaskUpdate(
  io: SocketServer,
  taskId: string,
  task: any,
  changes: any,
  updatedBy: string
) {
  io.to(`task:${taskId}`).emit('task-updated', {
    task,
    changes,
    updatedBy,
    timestamp: new Date().toISOString()
  });
}
```

## 部署和DevOps

### 1. Docker容器化

#### 多阶段构建Dockerfile

```dockerfile
# Frontend Dockerfile
FROM node:18-alpine AS frontend-builder

WORKDIR /app

# 复制package文件
COPY package*.json ./
RUN npm ci --only=production

# 复制源代码
COPY . .

# 构建前端
RUN npm run build

# 生产环境镜像
FROM nginx:alpine AS frontend-production

# 复制构建结果
COPY --from=frontend-builder /app/dist /usr/share/nginx/html

# 复制nginx配置
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

---

# Backend Dockerfile
FROM node:18-alpine AS backend-builder

WORKDIR /app

# 复制package文件
COPY package*.json ./
COPY prisma ./prisma/

# 安装依赖
RUN npm ci --only=production

# 生成Prisma客户端
RUN npx prisma generate

# 复制源代码
COPY . .

# 构建TypeScript
RUN npm run build

# 生产环境镜像
FROM node:18-alpine AS backend-production

WORKDIR /app

# 创建非root用户
RUN addgroup -g 1001 -S nodejs
RUN adduser -S taskflow -u 1001

# 复制依赖和构建结果
COPY --from=backend-builder --chown=taskflow:nodejs /app/node_modules ./node_modules
COPY --from=backend-builder --chown=taskflow:nodejs /app/dist ./dist
COPY --from=backend-builder --chown=taskflow:nodejs /app/prisma ./prisma
COPY --from=backend-builder --chown=taskflow:nodejs /app/package*.json ./

USER taskflow

EXPOSE 3001

CMD ["npm", "start"]
```

#### Docker Compose配置

```yaml
# docker-compose.yml
version: '3.8'

services:
  # PostgreSQL数据库
  postgres:
    image: postgres:15-alpine
    container_name: taskflow-postgres
    environment:
      POSTGRES_DB: taskflow
      POSTGRES_USER: taskflow
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    networks:
      - taskflow-network
    restart: unless-stopped

  # Redis缓存
  redis:
    image: redis:7-alpine
    container_name: taskflow-redis
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    networks:
      - taskflow-network
    restart: unless-stopped

  # 后端API服务
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: backend-production
    container_name: taskflow-backend
    environment:
      NODE_ENV: production
      DATABASE_URL: postgresql://taskflow:${POSTGRES_PASSWORD}@postgres:5432/taskflow
      REDIS_URL: redis://:${REDIS_PASSWORD}@redis:6379
      JWT_SECRET: ${JWT_SECRET}
      CLAUDE_API_KEY: ${CLAUDE_API_KEY}
      SENDGRID_API_KEY: ${SENDGRID_API_KEY}
    depends_on:
      - postgres
      - redis
    ports:
      - "3001:3001"
    networks:
      - taskflow-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3001/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # 前端应用
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: frontend-production
    container_name: taskflow-frontend
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - backend
    networks:
      - taskflow-network
    restart: unless-stopped
    volumes:
      - ./ssl:/etc/nginx/ssl:ro

  # Nginx负载均衡器
  nginx:
    image: nginx:alpine
    container_name: taskflow-nginx
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - frontend
      - backend
    networks:
      - taskflow-network
    restart: unless-stopped

  # 监控服务
  prometheus:
    image: prom/prometheus:latest
    container_name: taskflow-prometheus
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    networks:
      - taskflow-network
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: taskflow-grafana
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD}
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/grafana/provisioning:/etc/grafana/provisioning
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    networks:
      - taskflow-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:

networks:
  taskflow-network:
    driver: bridge
```

### 2. CI/CD Pipeline

#### GitHub Actions工作流

```yaml
# .github/workflows/deploy.yml
name: Deploy TaskFlow AI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: taskflow_test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: |
          cd backend && npm ci
          cd ../frontend && npm ci

      - name: Run backend tests
        run: |
          cd backend
          npm run test
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/taskflow_test

      - name: Run frontend tests
        run: |
          cd frontend
          npm run test

      - name: Run E2E tests
        run: |
          cd frontend
          npm run test:e2e

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=sha

      - name: Build and push backend image
        uses: docker/build-push-action@v5
        with:
          context: ./backend
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}/backend:${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}

      - name: Build and push frontend image
        uses: docker/build-push-action@v5
        with:
          context: ./frontend
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}/frontend:${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}

  deploy-staging:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    environment: staging

    steps:
      - name: Deploy to staging
        run: |
          echo "Deploying to staging environment..."
          # 这里可以添加部署到staging环境的脚本

  deploy-production:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
      - name: Deploy to production
        run: |
          echo "Deploying to production environment..."
          # 这里可以添加部署到生产环境的脚本

      - name: Run smoke tests
        run: |
          echo "Running smoke tests..."
          # 添加生产环境烟雾测试
```

## 总结：全栈开发的AI革命

通过TaskFlow AI项目的完整实践，你已经掌握了：

### 🎯 现代全栈核心技能

1. **前端现代化开发**：React 18 + TypeScript + Tailwind CSS的最佳实践
2. **后端架构设计**：Node.js + Express + Prisma的企业级架构
3. **AI集成开发**：Claude API的深度集成和智能功能实现
4. **实时协作功能**：WebSocket驱动的实时同步和协作
5. **DevOps最佳实践**：Docker容器化和CI/CD自动化部署

### ⚡ AI增强的开发效率

| 开发环节 | 传统方式 | AI增强方式 | 效率提升 |
|---------|----------|------------|------------|
| 需求分析 | 人工分析，经验依赖 | AI辅助分析，智能建议 | 分析速度3-5倍 |
| 代码生成 | 手写代码，查找文档 | AI生成框架，智能补全 | 编码速度5-10倍 |
| 业务逻辑 | 逐步实现，反复测试 | AI推荐方案，快速验证 | 开发速度2-3倍 |
| 用户体验 | 人工设计，A/B测试 | AI个性化，智能推荐 | 用户体验2倍+ |
| 运维部署 | 手动配置，经验调优 | 智能配置，自动优化 | 部署效率5倍+ |

### 🛠️ 全栈技术生态

- **前端技术栈**：React、TypeScript、Tailwind CSS、Vite、React Query
- **后端技术栈**：Node.js、Express、TypeScript、Prisma、PostgreSQL
- **AI集成**：Claude API、智能推荐、自动分析、优化建议
- **实时功能**：WebSocket、Socket.io、实时协作、消息推送
- **部署运维**：Docker、Nginx、CI/CD、监控告警

### 🚀 全栈发展趋势

1. **AI原生开发**：AI不再是附加功能，而是核心驱动力
2. **低代码/无代码**：可视化开发工具和AI辅助编程
3. **边缘计算集成**：前端AI推理和边缘计算能力
4. **实时协作标准**：实时同步成为Web应用标配
5. **全栈TypeScript**：类型安全贯穿整个应用栈

通过Claude Code的全栈开发实践，我们实现了从**传统开发到AI增强开发**，从**单一技能到全栈能力**的跃升。这不仅提高了开发效率，更为现代Web应用开发树立了新的标准。

在下一篇文章中，我们将探索微服务架构项目实践，学习如何构建可扩展的分布式系统。

## 相关文章推荐

- [监控与运维：生产环境最佳实践](27-监控与运维生产环境最佳实践.md)
- [微服务架构项目实践](29-微服务架构项目实践.md)
- [DevOps工具链集成案例](32-DevOps工具链集成案例.md)
- [性能优化与调试技巧](36-性能优化与调试技巧.md)

---

*本文是《Claude Code 完整教程系列》的第二十八部分。掌握了全栈Web应用开发，让我们继续探索微服务架构的奥秘！*