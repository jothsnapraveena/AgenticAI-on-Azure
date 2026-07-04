# Implementation Steps

## Step 1: Sign in through the Azure portal
Go to `https://portal.azure.com` and sign in with your Entra ID account.

A note on why this step differs from what you might expect: going straight to `ai.azure.com` first drops you on a generic "Create smarter agents with Microsoft Foundry" landing page. Clicking "Create an agent" there prompts "You'll need an Azure subscription to continue" and routes you into a subscription-creation flow before you've even created a Foundry resource. It's not wrong, but it's the harder path — going through the Azure portal first, where your subscription already exists, avoids that detour entirely.

## Step 2: Navigate to Microsoft Foundry
From the Azure portal, search for **Microsoft Foundry** in the top search bar, or navigate via **Home > Microsoft Foundry**. You'll land on the "Innovate Anywhere with AI" overview page, with three options: Create a Foundry Resource, Manage AI Resources, Explore Best Practices and Guidance.

## Step 3: Create the hub (labeled "Azure AI hub" in the creation blade)
A naming note before you start: the creation form itself is titled **Azure AI hub**, not "Foundry hub" — this is legacy AI Studio branding that hasn't been fully renamed in the portal yet, even though the breadcrumb above it reads "Microsoft Foundry | AI Hubs." Same underlying resource, older label. Don't let it make you think you're in the wrong place.

1. Select **Create a resource** under "Create a Foundry Resource"
2. On the **Basics** tab, fill in:
   - **Subscription** — your subscription
   - **Resource group** — select existing or **Create new**
   - **Region** — e.g., East US
   - **Name** — e.g., `hub-foundry-fundamentals`
   - **Friendly name** — a display name, can differ from the resource name
   - **Default project resource group** — check **Same as hub resource group** unless you have a reason to separate them
3. Under **Azure AI services base models**, you must connect an AI Services resource (this is what backs OpenAI and other model access) — select an existing one or **Create new**. This field is required; you cannot skip it.
4. Other tabs (Storage, Inbound Access, Outbound Access, Encryption, Identity, Tags) can be left at their defaults for this lab
5. Go to **Review + create**, then **Create**
6. Wait for "Your deployment is complete." This single deployment provisions **four resources**, not one: the hub itself, a Cognitive Services account, a Storage account, and a Key Vault. All four should show status **OK**.

## Step 4: Launch Foundry and create your project
1. From the completed deployment, select **Go to resource** to open the hub
2. On the hub's overview page, select **Launch Azure AI Foundry**
3. This opens the hub's **Management center** in ai.azure.com
4. Select **New project**
5. In the "Name your project" dialog, confirm the **Current hub** shown matches the hub you just created, then enter a **Project name**
6. Select **Create**

## Step 5: Confirm you've landed in the project
After creation, you should land on the project's **Overview** page in ai.azure.com, showing Endpoints and keys, Project details (connection string, subscription, resource group, location), and a left navigation with Model catalog, Playgrounds, and AI Services.

## Step 6: Locate RBAC settings
1. Back in the Azure portal, open the hub resource, then go to **Access control (IAM)**
2. Note the roles currently assigned (check **My access** and **View my access** if unsure)
3. Compare against project-level access if you want to see hub-vs-project scoping in practice

## Step 7: Locate the hub's Management center and the project's nav groups
1. From ai.azure.com, click the hub name dropdown near the top to reach the **Management center** — this is the hub-level fleet view (Overview, Users, Models + endpoints, Connected resources, Compute)
2. Back in your project, note the three left-navigation groups: **Build and customize**, **Observe and optimize**, **Protect and govern**
3. Don't configure anything in these yet — Build and customize is covered from Session 5 onward, Observe and optimize in Sessions 20-21, and Protect and govern in Sessions 18-19

This is where Session 1 ends. You now have a working hub and project — Session 2 picks up from here with the model catalog.
