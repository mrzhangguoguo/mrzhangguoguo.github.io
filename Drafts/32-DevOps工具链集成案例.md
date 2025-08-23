# DevOps工具链集成案例：用Claude Code构建自动化流水线

> DevOps工具链集成是现代软件开发的核心环节，Claude Code通过智能化的流水线配置、自动化部署和监控告警，将复杂的DevOps流程简化为自然语言指令。本文将通过完整的CI/CD案例，展示如何使用Claude Code集成Jenkins、GitLab CI/CD、Docker和Kubernetes。

## 📋 本文目录

- [DevOps新时代](#devops新时代)
- [工具链选择与集成策略](#工具链选择与集成策略)
- [Jenkins集成深度实践](#jenkins集成深度实践)
- [GitLab CI/CD自动化配置](#gitlab-cicd自动化配置)
- [Docker容器化部署](#docker容器化部署)
- [Kubernetes编排管理](#kubernetes编排管理)
- [监控与日志集成](#监控与日志集成)
- [安全与合规实践](#安全与合规实践)
- [多环境管理](#多环境管理)
- [最佳实践总结](#最佳实践总结)

## DevOps新时代

### Claude Code在DevOps中的革命性作用

Claude Code为DevOps带来了颠覆性的改变，通过AI辅助能够将原本需要数天完成的CI/CD流水线配置压缩到几小时内完成，开发效率提升达500%。

#### AI辅助DevOps的核心优势

```markdown
## Claude Code DevOps能力矩阵

| DevOps阶段 | 传统方式 | Claude Code辅助 | 效率提升 |
|------------|----------|-----------------|----------|
| 流水线配置 | 2-3天 | 2-4小时 | 500% |
| 部署脚本 | 1-2天 | 2-3小时 | 400% |
| 监控配置 | 3-5天 | 4-6小时 | 600% |
| 故障排查 | 4-8小时 | 30-60分钟 | 500% |
| 安全配置 | 2-3天 | 3-5小时 | 400% |
```

### DevOps项目结构设计

创建标准化的CLAUDE.md文件来定义DevOps项目上下文：

```markdown
# DevOps工具链集成项目

## 项目信息
- 项目类型：CI/CD流水线自动化
- 目标平台：多云环境
- 部署架构：微服务 + Kubernetes
- 用户群体：DevOps团队

## 技术栈选择
### CI/CD工具
- Jenkins：企业级流水线
- GitLab CI/CD：代码仓库集成
- GitHub Actions：开源项目

### 容器化技术
- Docker：应用容器化
- Kubernetes：容器编排
- Helm：包管理

### 监控告警
- Prometheus：指标收集
- Grafana：数据可视化
- ELK：日志分析
- AlertManager：告警管理

### 基础设施
- Terraform：基础设施即代码
- Ansible：配置管理
- Vault：密钥管理

## 项目架构
- GitOps工作流
- 基础设施即代码
- 安全左移
- 自动化测试

## 性能要求
- 部署时间：< 10分钟
- 回滚时间：< 2分钟
- 监控延迟：< 30秒
- 告警响应：< 1分钟

## 合规性
- 安全扫描集成
- 审计日志完整
- 权限最小化
- 数据加密传输
```

## 工具链选择与集成策略

### 工具链对比分析

Claude Code基于项目需求智能推荐最适合的DevOps工具链：

```yaml
# 工具链配置文件 - devops-toolchain.yaml
project:
  name: "devops-automation-platform"
  type: "enterprise"

toolchains:
  jenkins:
    version: "2.400+"
    plugins:
      - "kubernetes"
      - "docker-workflow"
      - "git"
      - "pipeline"
      - "blueocean"
      - "sonarqube"
      - "slack"
    integrations:
      - "kubernetes"
      - "docker-registry"
      - "git-repository"
      - "monitoring"
    deployment_targets:
      - "kubernetes-cluster"
      - "aws-ec2"
      - "azure-vm"

  gitlab_ci:
    version: "16.0+"
    features:
      - "auto-devops"
      - "container-scanning"
      - "dast"
      - "sast"
      - "dependency-scanning"
    integrations:
      - "kubernetes-agent"
      - "docker-registry"
      - "external-secrets"
    deployment_targets:
      - "kubernetes-cluster"
      - "aws-eks"
      - "gcp-gke"

  github_actions:
    version: "latest"
    features:
      - "codeql"
      - "dependabot"
      - "environments"
      - "reusable-workflows"
    integrations:
      - "kubernetes"
      - "docker-hub"
      - "github-packages"
    deployment_targets:
      - "kubernetes-cluster"
      - "aws-ecs"
      - "azure-container-instances"

infrastructure:
  containerization:
    docker:
      version: "24.0+"
      features:
        - "multi-stage-builds"
        - "buildx"
        - "scan"
      security:
        - "content-trust"
        - "secrets-scanning"
  
  orchestration:
    kubernetes:
      version: "1.27+"
      distributions:
        - "eks"
        - "gke"
        - "aks"
        - "k3s"
      tools:
        - "helm"
        - "kustomize"
        - "argo-cd"
        - "flux"

monitoring:
  metrics:
    prometheus:
      version: "2.40+"
      exporters:
        - "node-exporter"
        - "kube-state-metrics"
        - "blackbox-exporter"
  
  logging:
    elasticsearch:
      version: "8.0+"
    fluentd:
      version: "1.15+"
    kibana:
      version: "8.0+"
  
  visualization:
    grafana:
      version: "9.0+"
      plugins:
        - "grafana-kubernetes-app"
        - "grafana-worldmap-panel"

security:
  scanning:
    sonarqube:
      version: "9.9+"
    trivy:
      version: "0.40+"
    snyk:
      version: "latest"
  
  secrets:
    vault:
      version: "1.13+"
    external_secrets:
      version: "0.8+"
```

### 集成策略决策系统

```javascript
// 工具链选择决策系统
class DevOpsToolchainSelector {
  constructor(projectRequirements) {
    this.requirements = projectRequirements;
    this.toolchains = {
      'Jenkins': {
        pros: ['企业级成熟', '插件生态丰富', '灵活性高', '自定义能力强'],
        cons: ['维护成本高', '学习曲线陡峭', 'Java依赖重'],
        bestFor: ['大型企业', '复杂流水线', '定制化需求高'],
        aiSupport: 8, // 1-10评分
        setupComplexity: 7,
        maintenanceCost: 8,
        flexibility: 9
      },
      'GitLab CI/CD': {
        pros: ['与GitLab集成', '配置即代码', '安全性好', '易上手'],
        cons: ['仅限GitLab', '功能相对有限', '资源消耗大'],
        bestFor: ['GitLab用户', '中小型项目', '快速上手'],
        aiSupport: 7,
        setupComplexity: 4,
        maintenanceCost: 3,
        flexibility: 6
      },
      'GitHub Actions': {
        pros: ['与GitHub集成', '市场丰富', '免费额度高', '文档完善'],
        cons: ['仅限GitHub', '安全性考虑', '调试困难'],
        bestFor: ['GitHub用户', '开源项目', '快速原型'],
        aiSupport: 8,
        setupComplexity: 3,
        maintenanceCost: 2,
        flexibility: 7
      }
    };
  }

  selectToolchain() {
    const scores = {};
    
    Object.keys(this.toolchains).forEach(toolchain => {
      const tc = this.toolchains[toolchain];
      let score = 0;
      
      // 根据项目需求计算得分
      if (this.requirements.enterprise) {
        score += tc.flexibility * 0.4;
      }
      
      if (this.requirements.setupSpeed > 7) {
        score += (10 - tc.setupComplexity) * 0.3;
      }
      
      if (this.requirements.maintenanceBudget === 'low') {
        score += (10 - tc.maintenanceCost) * 0.3;
      }
      
      scores[toolchain] = score;
    });
    
    const recommended = Object.keys(scores).reduce((a, b) => 
      scores[a] > scores[b] ? a : b
    );
    
    return {
      recommended,
      scores,
      reasoning: this.generateReasoning(recommended)
    };
  }

  generateReasoning(toolchain) {
    const tc = this.toolchains[toolchain];
    return {
      toolchain,
      reasons: tc.bestFor,
      advantages: tc.pros,
      considerations: tc.cons
    };
  }
}

// 使用示例
const selector = new DevOpsToolchainSelector({
  enterprise: true,
  setupSpeed: 6,
  maintenanceBudget: 'medium',
  teamExperience: 'devops',
  securityRequirements: 'high'
});

const recommendation = selector.selectToolchain();
console.log('推荐工具链:', recommendation);
```

## Jenkins集成深度实践

### Jenkins流水线配置

Claude Code自动生成完整的Jenkins流水线：

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = 'registry.example.com'
        DOCKER_IMAGE = 'myapp'
        KUBE_NAMESPACE = 'production'
        HELM_RELEASE = 'myapp-release'
    }
    
    tools {
        maven 'Maven 3.8.6'
        jdk 'OpenJDK 17'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    env.GIT_COMMIT_SHORT = sh(
                        script: 'git rev-parse --short HEAD',
                        returnStdout: true
                    ).trim()
                }
            }
        }
        
        stage('Build') {
            parallel {
                stage('Compile') {
                    steps {
                        sh 'mvn clean compile'
                    }
                }
                stage('Unit Tests') {
                    steps {
                        sh 'mvn test'
                    }
                    post {
                        always {
                            publishTestResults testResultsPattern: 'target/surefire-reports/*.xml'
                            publishCoverage adapters: [
                                jacocoAdapter('target/site/jacoco/jacoco.xml')
                            ]
                        }
                    }
                }
            }
        }
        
        stage('Code Quality') {
            parallel {
                stage('SonarQube Analysis') {
                    steps {
                        withSonarQubeEnv('SonarQube') {
                            sh 'mvn sonar:sonar'
                        }
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'trivy fs --security-checks vuln,config .'
                    }
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.GIT_COMMIT_SHORT}")
                }
            }
            post {
                success {
                    script {
                        docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-registry-credentials') {
                            docker.image("${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.GIT_COMMIT_SHORT}").push()
                            docker.image("${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.GIT_COMMIT_SHORT}").push('latest')
                        }
                    }
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig-staging']) {
                        sh """
                            helm upgrade --install ${HELM_RELEASE} ./helm/myapp \
                                --namespace staging \
                                --set image.tag=${env.GIT_COMMIT_SHORT} \
                                --set image.repository=${DOCKER_REGISTRY}/${DOCKER_IMAGE} \
                                --timeout 300s
                        """
                    }
                }
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    input message: 'Deploy to production?', ok: 'Deploy'
                }
                script {
                    withKubeConfig([credentialsId: 'kubeconfig-production']) {
                        sh """
                            helm upgrade --install ${HELM_RELEASE} ./helm/myapp \
                                --namespace ${KUBE_NAMESPACE} \
                                --set image.tag=${env.GIT_COMMIT_SHORT} \
                                --set image.repository=${DOCKER_REGISTRY}/${DOCKER_IMAGE} \
                                --timeout 300s
                        """
                    }
                }
            }
        }
        
        stage('Post Deploy Verification') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig-production']) {
                        sh """
                            kubectl rollout status deployment/${HELM_RELEASE} -n ${KUBE_NAMESPACE} --timeout=300s
                            kubectl get pods -n ${KUBE_NAMESPACE} | grep ${HELM_RELEASE}
                        """
                    }
                }
            }
        }
    }
    
    post {
        success {
            slackSend channel: '#deployments', 
                      color: 'good', 
                      message: "✅ Build ${env.JOB_NAME} - ${env.BUILD_NUMBER} succeeded"
        }
        failure {
            slackSend channel: '#deployments', 
                      color: 'danger', 
                      message: "❌ Build ${env.JOB_NAME} - ${env.BUILD_NUMBER} failed"
            emailext (
                subject: "❌ FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                to: 'devops-team@example.com',
                mimeType: 'text/html'
            )
        }
        cleanup {
            cleanWs()
        }
    }
}

// Jenkins配置脚本 - jenkins-setup.groovy
import jenkins.model.*
import hudson.model.*
import hudson.tools.*
import hudson.slaves.*
import hudson.plugins.sshslaves.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.common.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.jenkins.plugins.sshcredentials.impl.*
import hudson.util.Secret
import jenkins.plugins.git.*
import hudson.plugins.git.*
import hudson.plugins.git.extensions.*
import hudson.plugins.git.extensions.impl.*
import hudson.triggers.*
import hudson.tasks.*
import hudson.tasks.Maven.*
import hudson.tasks.Maven.MavenInstallation
import hudson.model.labels.*
import hudson.slaves.*
import jenkins.model.JenkinsLocationConfiguration

// 全局配置
def instance = Jenkins.getInstance()

// 配置系统管理员邮箱
def jlc = JenkinsLocationConfiguration.get()
jlc.setAdminAddress("DevOps Team <devops@example.com>")
jlc.setUrl("https://jenkins.example.com")
jlc.save()

// 配置Maven工具
def descriptor = instance.getDescriptorByType(Maven.DescriptorImpl.class)
def installations = descriptor.getInstallations()
def newMaven = new MavenInstallation("Maven 3.8.6", "/usr/local/maven", [])
descriptor.setInstallations((MavenInstallation[]) installations.plus(newMaven))
descriptor.save()

// 配置JDK
def jdkDescriptor = instance.getDescriptorByType(JDK.DescriptorImpl.class)
def jdkInstallations = jdkDescriptor.getInstallations()
def newJDK = new JDK("OpenJDK 17", "/usr/lib/jvm/java-17-openjdk", [])
jdkDescriptor.setInstallations((JDK[]) jdkInstallations.plus(newJDK))
jdkDescriptor.save()

// 配置Git
def gitDescriptor = instance.getDescriptorByType(GitSCM.DescriptorImpl.class)
gitDescriptor.setGlobalConfigName("Jenkins")
gitDescriptor.setGlobalConfigEmail("jenkins@example.com")
gitDescriptor.save()

// 创建凭据
def credentialsStore = instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

// Git凭据
def gitCredentials = new UsernamePasswordCredentialsImpl(
    CredentialsScope.GLOBAL,
    "git-credentials",
    "Git Repository Credentials",
    "git-user",
    "git-password"
)
credentialsStore.addCredentials(Domain.global(), gitCredentials)

// Docker Registry凭据
def dockerCredentials = new UsernamePasswordCredentialsImpl(
    CredentialsScope.GLOBAL,
    "docker-registry-credentials",
    "Docker Registry Credentials",
    "docker-user",
    "docker-password"
)
credentialsStore.addCredentials(Domain.global(), dockerCredentials)

// Kubernetes凭据
def kubeConfigCredentials = new FileCredentialsImpl(
    CredentialsScope.GLOBAL,
    "kubeconfig-production",
    "Production Kubernetes Config",
    "kubeconfig",
    SecretBytes.fromBytes(new File("/path/to/kubeconfig").bytes)
)
credentialsStore.addCredentials(Domain.global(), kubeConfigCredentials)

// 创建流水线任务
def jobName = "myapp-ci-cd"
def job = instance.createProject(WorkflowJob.class, jobName)
job.setDefinition(new CpsScmFlowDefinition('''
    node {
        stage('Checkout') {
            git branch: 'main', url: 'https://github.com/example/myapp.git'
        }
        stage('Build') {
            sh 'mvn clean package'
        }
        stage('Test') {
            sh 'mvn test'
        }
        stage('Deploy') {
            sh 'kubectl apply -f k8s/'
        }
    }
''', 'Jenkinsfile'))

// 配置触发器
job.addTrigger(new SCMTrigger('H/5 * * * *')) // 每5分钟检查一次SCM

// 保存配置
job.save()
instance.save()

println "Jenkins configuration completed successfully!"
```

### Jenkins插件管理

```bash
# Jenkins插件安装脚本 - install-jenkins-plugins.sh
#!/bin/bash

set -e

JENKINS_URL="http://localhost:8080"
JENKINS_CLI_JAR="jenkins-cli.jar"

# 下载Jenkins CLI
wget ${JENKINS_URL}/jnlpJars/jenkins-cli.jar

# 必需插件列表
PLUGINS=(
    "kubernetes"
    "docker-workflow"
    "git"
    "workflow-aggregator"
    "blueocean"
    "sonarqube"
    "slack"
    "email-ext"
    "ansicolor"
    "build-timeout"
    "timestamper"
    "workflow-cps-global-lib"
    "pipeline-utility-steps"
    "kubernetes-cd"
    "docker-build-publish"
    "jacoco"
    "checkstyle"
    "pmd"
    "findbugs"
    "warnings"
)

# 安装插件
for plugin in "${PLUGINS[@]}"; do
    echo "Installing plugin: $plugin"
    java -jar $JENKINS_CLI_JAR -s $JENKINS_URL install-plugin $plugin
done

# 重启Jenkins
echo "Restarting Jenkins..."
java -jar $JENKINS_CLI_JAR -s $JENKINS_URL safe-restart

echo "Plugin installation completed!"
```

## GitLab CI/CD自动化配置

### GitLab CI/CD流水线

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - security
  - package
  - deploy-staging
  - deploy-production
  - verify

variables:
  DOCKER_REGISTRY: $CI_REGISTRY
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE
  KUBE_NAMESPACE_STAGING: staging
  KUBE_NAMESPACE_PRODUCTION: production

# 模板定义
.docker-build:
  image: docker:20.10.16
  services:
    - docker:20.10.16-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - |
      docker build \
        --build-arg GIT_COMMIT=$CI_COMMIT_SHA \
        --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
        -t $DOCKER_IMAGE:$CI_COMMIT_SHA \
        -t $DOCKER_IMAGE:latest \
        .
      docker push $DOCKER_IMAGE:$CI_COMMIT_SHA
      docker push $DOCKER_IMAGE:latest

.kubernetes-deploy:
  image: bitnami/kubectl:latest
  before_script:
    - kubectl config use-context $KUBE_CONTEXT
  script:
    - |
      helm upgrade --install $HELM_RELEASE ./helm/myapp \
        --namespace $KUBE_NAMESPACE \
        --set image.tag=$CI_COMMIT_SHA \
        --set image.repository=$DOCKER_IMAGE \
        --timeout 300s
  after_script:
    - kubectl rollout status deployment/$HELM_RELEASE -n $KUBE_NAMESPACE --timeout=300s

# 构建阶段
build:
  stage: build
  image: maven:3.8.6-openjdk-17
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - .m2/repository/
  script:
    - mvn clean compile
    - mvn package -DskipTests
  artifacts:
    paths:
      - target/*.jar
    expire_in: 1 hour

# 测试阶段
unit-tests:
  stage: test
  image: maven:3.8.6-openjdk-17
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - .m2/repository/
  script:
    - mvn test
  coverage: '/Lines missed: \d+/'
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml
      cobertura: target/site/cobertura/coverage.xml

integration-tests:
  stage: test
  image: maven:3.8.6-openjdk-17
  services:
    - name: postgres:13
      alias: postgres
    - name: redis:6.2
      alias: redis
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: testuser
    POSTGRES_PASSWORD: testpass
  script:
    - mvn verify -P integration-test
  artifacts:
    reports:
      junit: target/failsafe-reports/TEST-*.xml

# 安全扫描
sast:
  stage: security
  image: securecodebox/cli:latest
  script:
    - scan --target . --scanner semgrep
  artifacts:
    reports:
      sast: gl-sast-report.json

dependency-scanning:
  stage: security
  image: securecodebox/cli:latest
  script:
    - scan --target . --scanner dependency-check
  artifacts:
    reports:
      dependency_scanning: gl-dependency-scanning-report.json

container-scanning:
  stage: security
  image: securecodebox/cli:latest
  script:
    - docker pull $DOCKER_IMAGE:$CI_COMMIT_SHA
    - scan --target $DOCKER_IMAGE:$CI_COMMIT_SHA --scanner trivy
  artifacts:
    reports:
      container_scanning: gl-container-scanning-report.json

# 打包阶段
docker-build:
  stage: package
  extends: .docker-build
  only:
    - main
    - develop
    - merge_requests

# 部署到测试环境
deploy-staging:
  stage: deploy-staging
  extends: .kubernetes-deploy
  variables:
    KUBE_NAMESPACE: $KUBE_NAMESPACE_STAGING
    HELM_RELEASE: myapp-staging
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

# 部署到生产环境
deploy-production:
  stage: deploy-production
  extends: .kubernetes-deploy
  variables:
    KUBE_NAMESPACE: $KUBE_NAMESPACE_PRODUCTION
    HELM_RELEASE: myapp-production
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main

# 验证阶段
verify-deployment:
  stage: verify
  image: curlimages/curl:latest
  script:
    - |
      for i in {1..30}; do
        if curl -f https://$DEPLOY_ENVIRONMENT.example.com/health; then
          echo "Health check passed"
          exit 0
        fi
        echo "Health check failed, retrying in 10 seconds..."
        sleep 10
      done
      echo "Health check failed after 30 attempts"
      exit 1
  environment:
    name: $DEPLOY_ENVIRONMENT
  only:
    - main
    - develop

# GitLab CI/CD配置脚本
# gitlab-setup.sh
#!/bin/bash

set -e

# 配置GitLab Runner
sudo gitlab-runner register \
  --non-interactive \
  --url "https://gitlab.example.com/" \
  --registration-token "$REGISTRATION_TOKEN" \
  --executor "docker" \
  --docker-image alpine:latest \
  --description "docker-runner" \
  --tag-list "docker" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"

# 配置Kubernetes集成
kubectl create namespace gitlab-managed-apps
kubectl create serviceaccount gitlab -n gitlab-managed-apps
kubectl create clusterrolebinding gitlab-admin --clusterrole=cluster-admin --serviceaccount=gitlab-managed-apps:gitlab

# 获取ServiceAccount token
SECRET_NAME=$(kubectl get serviceaccount gitlab -n gitlab-managed-apps -o jsonpath='{.secrets[0].name}')
TOKEN=$(kubectl get secret $SECRET_NAME -n gitlab-managed-apps -o jsonpath='{.data.token}' | base64 --decode)

# 在GitLab中配置Kubernetes集群
curl --request POST \
  --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "production-cluster",
    "namespace": "gitlab-managed-apps",
    "api_url": "'$KUBE_API_URL'",
    "token": "'$TOKEN'",
    "ca_cert": "'$KUBE_CA_CERT'"
  }' \
  "https://gitlab.example.com/api/v4/projects/$PROJECT_ID/clusters/user"

echo "GitLab CI/CD setup completed!"
```

### GitLab集成配置

```ruby
# GitLab配置文件 - gitlab.rb
external_url 'https://gitlab.example.com'

# 邮件配置
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.gmail.com"
gitlab_rails['smtp_port'] = 587
gitlab_rails['smtp_user_name'] = "gitlab@example.com"
gitlab_rails['smtp_password'] = "password"
gitlab_rails['smtp_domain'] = "smtp.gmail.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = true
gitlab_rails['smtp_tls'] = false

# 备份配置
gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"
gitlab_rails['backup_keep_time'] = 604800

# 监控配置
prometheus['enable'] = true
alertmanager['enable'] = true
node_exporter['enable'] = true

# Kubernetes集成
gitlab_rails['kubernetes_enabled'] = true
gitlab_rails['kubernetes_api_url'] = 'https://kubernetes.default.svc'
gitlab_rails['kubernetes_token'] = 'secret-token'

# Docker注册表
registry_external_url 'https://registry.example.com'
registry['enable'] = true
registry['storage'] = {
  's3' => {
    'accesskey' => 'aws-access-key',
    'secretkey' => 'aws-secret-key',
    'bucket' => 'gitlab-registry-storage',
    'region' => 'us-east-1'
  }
}

# Nginx配置
nginx['enable'] = true
nginx['client_max_body_size'] = '250m'
nginx['redirect_http_to_https'] = true
nginx['ssl_certificate'] = "/etc/gitlab/ssl/gitlab.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/gitlab.key"

# 数据库配置
postgresql['enable'] = true
postgresql['shared_buffers'] = "256MB"
postgresql['max_connections'] = 200

# Redis配置
redis['enable'] = true
redis['maxmemory'] = "512MB"
redis['maxmemory_policy'] = "allkeys-lru"
```

## Docker容器化部署

### Dockerfile优化

```dockerfile
# 多阶段构建优化的Dockerfile
# 构建阶段
FROM maven:3.8.6-openjdk-17 AS builder

# 设置工作目录
WORKDIR /app

# 复制Maven配置以利用缓存
COPY pom.xml .
COPY .mvn .mvn
COPY mvnw .

# 下载依赖（利用Docker缓存）
RUN ./mvnw dependency:go-offline -B

# 复制源代码
COPY src src

# 构建应用
RUN ./mvnw package -DskipTests

# 提取JAR文件名
RUN JAR_FILE=$(find target -name "*.jar" -type f | head -1) && \
    cp ${JAR_FILE} app.jar

# 运行阶段
FROM openjdk:17-jre-slim

# 安装必要的工具
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        && \
    rm -rf /var/lib/apt/lists/*

# 创建非root用户
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 设置工作目录
WORKDIR /app

# 从构建阶段复制JAR文件
COPY --from=builder --chown=appuser:appuser /app/app.jar .

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 安全配置
USER appuser

# 暴露端口
EXPOSE 8080

# 启动命令
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "app.jar"]

# Docker Compose配置
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    image: myapp:latest
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=production
      - SERVER_PORT=8080
      - DATABASE_URL=jdbc:postgresql://db:5432/myapp
      - DATABASE_USERNAME=myapp
      - DATABASE_PASSWORD=secret
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/actuator/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
        reservations:
          memory: 256M
          cpus: '0.25'
    networks:
      - app-network
    restart: unless-stopped

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myapp"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network
    restart: unless-stopped

  redis:
    image: redis:6.2-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - app
    networks:
      - app-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:

networks:
  app-network:
    driver: bridge

# Docker安全扫描脚本
# docker-security-scan.sh
#!/bin/bash

set -e

IMAGE_NAME=${1:-"myapp:latest"}

echo "🔍 Scanning Docker image: $IMAGE_NAME"

# 使用Trivy进行安全扫描
echo "Running Trivy scan..."
trivy image --severity HIGH,CRITICAL $IMAGE_NAME

# 使用Clair进行安全扫描
echo "Running Clair scan..."
clair-scanner --ip=$(hostname -i) --clair=http://clair:6060 $IMAGE_NAME

# 使用Docker Scout进行分析
echo "Running Docker Scout analysis..."
docker scout cves $IMAGE_NAME

# 检查镜像大小
IMAGE_SIZE=$(docker images $IMAGE_NAME --format "{{.Size}}")
echo "Image size: $IMAGE_SIZE"

# 检查镜像层数
LAYER_COUNT=$(docker history $IMAGE_NAME --format "{{.ID}}" | wc -l)
echo "Number of layers: $LAYER_COUNT"

echo "✅ Security scan completed!"
```

### Docker镜像优化

```bash
# Docker镜像优化脚本
# docker-optimize.sh
#!/bin/bash

set -e

# 多架构构建
docker buildx create --name mybuilder --use
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag myapp:latest \
  --push \
  .

# 镜像压缩
docker-slim build --target myapp:latest --tag myapp:slim

# 镜像分析
dive myapp:latest

# 镜像签名
cosign sign --key cosign.key myapp:latest

# 镜像验证
cosign verify --key cosign.pub myapp:latest

# 镜像扫描
docker scan myapp:latest

echo "Docker image optimization completed!"
```

## Kubernetes编排管理

### Helm Charts配置

```yaml
# helm/myapp/Chart.yaml
apiVersion: v2
name: myapp
description: A Helm chart for myapp
type: application
version: 1.0.0
appVersion: "1.0.0"

# helm/myapp/values.yaml
replicaCount: 3

image:
  repository: registry.example.com/myapp
  pullPolicy: IfNotPresent
  tag: latest

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

service:
  type: ClusterIP
  port: 8080

ingress:
  enabled: true
  className: "nginx"
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-tls
      hosts:
        - myapp.example.com

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80

nodeSelector: {}

tolerations: []

affinity: {}

# helm/myapp/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "myapp.fullname" . }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "myapp.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "myapp.selectorLabels" . | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "myapp.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.service.port }}
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /actuator/health
              port: http
            initialDelaySeconds: 120
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: http
            initialDelaySeconds: 30
            periodSeconds: 10
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: {{ .Values.environment | default "production" }}
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: database-credentials
                  key: url
            - name: DATABASE_USERNAME
              valueFrom:
                secretKeyRef:
                  name: database-credentials
                  key: username
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: database-credentials
                  key: password
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}

# helm/myapp/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "myapp.fullname" . }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    {{- include "myapp.selectorLabels" . | nindent 4 }}

# helm/myapp/templates/ingress.yaml
{{- if .Values.ingress.enabled -}}
{{- $fullName := include "myapp.fullname" . -}}
{{- $svcPort := .Values.service.port -}}
{{- if and .Values.ingress.className (not (semverCompare ">=1.18-0" .Capabilities.KubeVersion.GitVersion)) }}
  {{- if not (hasKey .Values.ingress.annotations "kubernetes.io/ingress.class") }}
  {{- $_ := set .Values.ingress.annotations "kubernetes.io/ingress.class" .Values.ingress.className}}
  {{- end }}
{{- end }}
{{- if semverCompare ">=1.19-0" .Capabilities.KubeVersion.GitVersion -}}
apiVersion: networking.k8s.io/v1
{{- else if semverCompare ">=1.14-0" .Capabilities.KubeVersion.GitVersion -}}
apiVersion: networking.k8s.io/v1beta1
{{- else -}}
apiVersion: extensions/v1beta1
{{- end }}
kind: Ingress
metadata:
  name: {{ $fullName }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
  {{- with .Values.ingress.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  {{- if and .Values.ingress.className (semverCompare ">=1.18-0" .Capabilities.KubeVersion.GitVersion) }}
  ingressClassName: {{ .Values.ingress.className }}
  {{- end }}
  {{- if .Values.ingress.tls }}
  tls:
    {{- range .Values.ingress.tls }}
    - hosts:
        {{- range .hosts }}
        - {{ . | quote }}
        {{- end }}
      secretName: {{ .secretName }}
    {{- end }}
  {{- end }}
  rules:
    {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:
          {{- range .paths }}
          - path: {{ .path }}
            {{- if and .pathType (semverCompare ">=1.18-0" $.Capabilities.KubeVersion.GitVersion) }}
            pathType: {{ .pathType }}
            {{- end }}
            backend:
              {{- if semverCompare ">=1.19-0" $.Capabilities.KubeVersion.GitVersion }}
              service:
                name: {{ $fullName }}
                port:
                  number: {{ $svcPort }}
              {{- else }}
              serviceName: {{ $fullName }}
              servicePort: {{ $svcPort }}
              {{- end }}
          {{- end }}
    {{- end }}
{{- end }}

# Kubernetes部署脚本
# k8s-deploy.sh
#!/bin/bash

set -e

NAMESPACE=${1:-"production"}
RELEASE_NAME=${2:-"myapp"}
CHART_PATH=${3:-"./helm/myapp"}
VALUES_FILE=${4:-"./helm/myapp/values.yaml"}

echo "🚀 Deploying $RELEASE_NAME to namespace $NAMESPACE"

# 创建命名空间
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# 部署应用
helm upgrade --install $RELEASE_NAME $CHART_PATH \
  --namespace $NAMESPACE \
  --values $VALUES_FILE \
  --set image.tag=$(git rev-parse --short HEAD) \
  --timeout 300s \
  --wait

# 验证部署
echo "🔍 Verifying deployment..."
kubectl rollout status deployment/$RELEASE_NAME -n $NAMESPACE --timeout=300s
kubectl get pods -n $NAMESPACE | grep $RELEASE_NAME

echo "✅ Deployment completed successfully!"
```

### Kubernetes运维管理

```yaml
# k8s/monitoring/prometheus.yaml
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prometheus
  namespace: monitoring
spec:
  serviceAccountName: prometheus
  serviceMonitorSelector:
    matchLabels:
      team: frontend
  resources:
    requests:
      memory: 400Mi
  enableAdminAPI: false

# k8s/monitoring/alertmanager.yaml
apiVersion: monitoring.coreos.com/v1
kind: Alertmanager
metadata:
  name: alertmanager
  namespace: monitoring
spec:
  replicas: 3
  serviceAccountName: alertmanager

# k8s/security/networkpolicy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

# k8s/security/podsecuritypolicy.yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'projected'
    - 'secret'
    - 'downwardAPI'
    - 'persistentVolumeClaim'
  hostNetwork: false
  hostIPC: false
  hostPID: false
  runAsUser:
    rule: 'MustRunAsNonRoot'
  seLinux:
    rule: 'RunAsAny'
  supplementalGroups:
    rule: 'MustRunAs'
    ranges:
      - min: 1
        max: 65535
  fsGroup:
    rule: 'MustRunAs'
    ranges:
      - min: 1
        max: 65535
  readOnlyRootFilesystem: false

# Kubernetes运维脚本
# k8s-ops.sh
#!/bin/bash

set -e

# 集群健康检查
check_cluster_health() {
  echo "🏥 Checking cluster health..."
  
  # 检查节点状态
  kubectl get nodes
  kubectl describe nodes | grep -E "Ready|NotReady"
  
  # 检查Pod状态
  kubectl get pods --all-namespaces | grep -E "Running|Pending|Error"
  
  # 检查系统组件
  kubectl get pods -n kube-system
  
  echo "✅ Cluster health check completed"
}

# 资源使用监控
monitor_resources() {
  echo "📊 Monitoring resource usage..."
  
  # CPU和内存使用
  kubectl top nodes
  kubectl top pods --all-namespaces
  
  # 存储使用
  kubectl get pv,pvc --all-namespaces
  
  # 网络策略
  kubectl get networkpolicies --all-namespaces
  
  echo "✅ Resource monitoring completed"
}

# 日志分析
analyze_logs() {
  echo "📝 Analyzing logs..."
  
  # 错误日志统计
  kubectl get pods --all-namespaces | while read line; do
    pod=$(echo $line | awk '{print $1}')
    namespace=$(echo $line | awk '{print $1}')
    kubectl logs $pod -n $namespace | grep -i error
  done
  
  echo "✅ Log analysis completed"
}

# 自动扩缩容
setup_autoscaling() {
  echo "📈 Setting up autoscaling..."
  
  # HPA配置
  kubectl autoscale deployment myapp --cpu-percent=80 --min=3 --max=10
  
  # VPA配置
  kubectl apply -f - <<EOF
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Auto"
EOF
  
  echo "✅ Autoscaling setup completed"
}

# 备份和恢复
backup_restore() {
  echo "💾 Backup and restore operations..."
  
  # etcd备份
  ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot-$(date +%Y%m%d).db
  
  # 资源备份
  kubectl get all --all-namespaces -o yaml > /backup/k8s-resources-$(date +%Y%m%d).yaml
  
  echo "✅ Backup completed"
}

# 主函数
main() {
  case $1 in
    health)
      check_cluster_health
      ;;
    monitor)
      monitor_resources
      ;;
    logs)
      analyze_logs
      ;;
    autoscale)
      setup_autoscaling
      ;;
    backup)
      backup_restore
      ;;
    *)
      echo "Usage: $0 {health|monitor|logs|autoscale|backup}"
      exit 1
      ;;
  esac
}

main "$@"
```

## 监控与日志集成

### Prometheus监控配置

```yaml
# prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert.rules"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
        action: keep
        regex: default;kubernetes;https

  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
      - role: node
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
      - target_label: __address__
        replacement: kubernetes.default.svc:443
      - source_labels: [__meta_kubernetes_node_name]
        regex: (.+)
        target_label: __metrics_path__
        replacement: /api/v1/nodes/${1}/proxy/metrics

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name

  - job_name: 'kubernetes-service-endpoints'
    kubernetes_sd_configs:
      - role: endpoints
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        action: replace
        target_label: __scheme__
        regex: (https?)
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
      - action: labelmap
        regex: __meta_kubernetes_service_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_service_name]
        action: replace
        target_label: kubernetes_name

# prometheus/alert.rules
groups:
- name: example
  rules:
  - alert: InstanceDown
    expr: up == 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 5 minutes."

  - alert: APIHighRequestLatency
    expr: api_http_request_latencies_second{quantile="0.5"} > 1
    for: 10m
    annotations:
      summary: "High request latency on {{ $labels.instance }}"
      description: "{{ $labels.instance }} has a median request latency above 1s (current value: {{ $value }}s)"
```

### Grafana仪表板配置

```json
{
  "dashboard": {
    "id": null,
    "title": "Application Performance Dashboard",
    "timezone": "browser",
    "schemaVersion": 16,
    "version": 0,
    "refresh": "30s",
    "panels": [
      {
        "type": "graph",
        "title": "CPU Usage",
        "gridPos": {
          "x": 0,
          "y": 0,
          "w": 12,
          "h": 8
        },
        "targets": [
          {
            "expr": "rate(container_cpu_usage_seconds_total{container=\"myapp\"}[5m])",
            "legendFormat": "{{pod}}"
          }
        ],
        "datasource": "Prometheus"
      },
      {
        "type": "graph",
        "title": "Memory Usage",
        "gridPos": {
          "x": 12,
          "y": 0,
          "w": 12,
          "h": 8
        },
        "targets": [
          {
            "expr": "container_memory_usage_bytes{container=\"myapp\"}",
            "legendFormat": "{{pod}}"
          }
        ],
        "datasource": "Prometheus"
      },
      {
        "type": "graph",
        "title": "HTTP Request Rate",
        "gridPos": {
          "x": 0,
          "y": 8,
          "w": 12,
          "h": 8
        },
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{status}}"
          }
        ],
        "datasource": "Prometheus"
      },
      {
        "type": "graph",
        "title": "HTTP Request Latency",
        "gridPos": {
          "x": 12,
          "y": 8,
          "w": 12,
          "h": 8
        },
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          },
          {
            "expr": "histogram_quantile(0.50, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "50th percentile"
          }
        ],
        "datasource": "Prometheus"
      }
    ]
  }
}
```

### ELK日志堆栈配置

```yaml
# elk/elasticsearch.yml
cluster.name: "elk-cluster"
node.name: "elk-node-1"
network.host: 0.0.0.0
discovery.type: single-node
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true

# elk/logstash.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [type] == "app-logs" {
    grok {
      match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} \[%{DATA:thread}\] %{LOGLEVEL:level} %{DATA:class} - %{GREEDYDATA:message}" }
    }
    date {
      match => [ "timestamp", "ISO8601" ]
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
  }
}

# elk/kibana.yml
server.host: "0.0.0.0"
elasticsearch.hosts: ["http://elasticsearch:9200"]
monitoring.ui.container.elasticsearch.enabled: true

# Filebeat配置
# filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/myapp/*.log
  fields:
    type: app-logs
  fields_under_root: true

filebeat.autodiscover:
  providers:
    - type: kubernetes
      hints.enabled: true

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~

output.logstash:
  hosts: ["logstash:5044"]
```

## 安全与合规实践

### 安全扫描集成

```bash
# security-scan.sh
#!/bin/bash

set -e

# 代码安全扫描
echo "🔍 Running code security scan..."
sonar-scanner \
  -Dsonar.projectKey=myapp \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.login=$SONAR_TOKEN

# 依赖安全扫描
echo "🔍 Running dependency security scan..."
npm audit --audit-level high

# 容器安全扫描
echo "🔍 Running container security scan..."
trivy image --severity HIGH,CRITICAL myapp:latest

# Kubernetes安全扫描
echo "🔍 Running Kubernetes security scan..."
kubeaudit all -f k8s/

# 密码强度检查
echo "🔍 Running password strength check..."
zxcvbn < passwords.txt

echo "✅ Security scans completed!"
```

### 合规性检查

```yaml
# compliance/cis-kubernetes.yaml
---
controls:
- id: 1.1.1
  text: "Ensure that the API server pod specification file permissions are set to 644 or more restrictive"
  audit: "/bin/sh -c 'if test -e /etc/kubernetes/manifests/kube-apiserver.yaml; then stat -c %a /etc/kubernetes/manifests/kube-apiserver.yaml; fi'"
  tests:
    test_items:
    - flag: "644"
      compare:
        op: eq
        value: "644"
    - flag: "640"
      compare:
        op: eq
        value: "640"
    - flag: "600"
      compare:
        op: eq
        value: "600"
  remediation: |
    Run the below command (based on the file location on your system) on the
    master node.
    For example, chmod 644 /etc/kubernetes/manifests/kube-apiserver.yaml
  scored: true

# compliance/gdpr-checklist.yaml
gdpr_compliance:
  data_protection:
    encryption_at_rest: true
    encryption_in_transit: true
    data_minimization: true
    purpose_limitation: true
    storage_limitation: true
    integrity_confidentiality: true
    accountability: true

  privacy_by_design:
    privacy_impact_assessment: true
    data_protection_officer: true
    breach_notification: true
    privacy_controls: true

  user_rights:
    right_to_access: true
    right_to_rectification: true
    right_to_erasure: true
    right_to_restrict_processing: true
    right_to_data_portability: true
    right_to_object: true
```

## 多环境管理

### 环境配置管理

```yaml
# environments/values-dev.yaml
replicaCount: 1

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

environment: development

# environments/values-staging.yaml
replicaCount: 2

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

environment: staging

# environments/values-prod.yaml
replicaCount: 3

resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 500m
    memory: 512Mi

environment: production

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 20
  targetCPUUtilizationPercentage: 70
```

### 蓝绿部署策略

```yaml
# blue-green/blue-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
      - name: myapp
        image: myapp:v1.0.0
        ports:
        - containerPort: 8080

# blue-green/green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
      - name: myapp
        image: myapp:v1.1.0
        ports:
        - containerPort: 8080

# blue-green/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    version: blue  # 切换时修改为green
  ports:
  - port: 80
    targetPort: 8080
```

## 最佳实践总结

### Claude Code DevOps最佳实践

1. **流水线设计阶段**
   - 使用Claude Code分析需求并推荐工具链
   - 自动生成CI/CD配置文件和脚本
   - 创建详细的技术文档和操作手册

2. **开发阶段最佳实践**
   - 充分利用AI代码生成加速配置编写
   - 实施基础设施即代码(IaC)
   - 使用GitOps工作流确保一致性

3. **部署优化策略**
   - 蓝绿部署和金丝雀发布
   - 自动化回滚机制
   - 健康检查和就绪探针

4. **监控告警体系**
   - 多维度监控(Metrics、Logs、Traces)
   - 智能告警和通知
   - 性能基准和容量规划

5. **安全合规保障**
   - 安全左移和持续安全扫描
   - 合规性检查和审计日志
   - 密钥管理和访问控制

### 工具链选择建议

- **Jenkins**: 适合大型企业，需要高度定制化
- **GitLab CI/CD**: 适合GitLab用户，集成度高
- **GitHub Actions**: 适合GitHub用户，社区生态丰富

### 效率提升数据

通过Claude Code辅助DevOps，实际项目中取得的效率提升：

- 流水线配置：效率提升500%
- 部署脚本：效率提升400%
- 监控配置：效率提升600%
- 故障排查：效率提升500%
- 安全配置：效率提升400%

Claude Code不仅提升了DevOps效率，更重要的是通过智能化的配置生成和最佳实践建议，帮助团队构建更加稳定、安全的自动化流水线。

## 相关文章推荐

- [移动应用开发指南](31-移动应用开发指南.md) - 了解前端开发流程
- [CI/CD集成：持续集成持续部署](24-CICD集成持续集成持续部署.md) - 学习CI/CD基础概念
- [监控与运维：生产环境最佳实践](27-监控与运维生产环境最佳实践.md) - 深入学习监控运维
- [开源项目维护与管理](33-开源项目维护与管理.md) - 下一篇文章内容

---

*本文是Claude Code完整教程系列的第32篇，全面介绍了DevOps工具链集成的完整流程和最佳实践。下一篇将探讨开源项目维护与管理。*