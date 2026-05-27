class OnionAgent:
    def __init__(self, policy_engine, notifier, auditor):
        self.policy_engine = policy_engine
        self.notifier = notifier
        self.auditor = auditor

    def observe(self, input_data):
        # L1: Input validation
        if not self._validate_input(input_data):
            self.auditor.log('rejected', reason='invalid input')
            raise Exception('Input validation failed')
        return input_data

    def notice(self, input_data):
        # L2: Threat/risk signal detection
        risk = self._analyze_signals(input_data)
        self.auditor.log('signal_check', risk_level=risk)
        if risk > self.policy_engine.max_risk:
            self.notifier.notify_guardian(f'High risk detected: {risk}')
            raise Exception('Risk too high')
        return True

    def infer(self, input_data):
        # L3: Policy decision
        decision, rationale = self.policy_engine.evaluate(input_data)
        self.auditor.log('decision', decision=decision, rationale=rationale)
        if not decision:
            self.notifier.notify_guardian('Policy denied action.')
            raise Exception('Policy decision: Denied')
        return decision

    def operate(self, action):
        # L4: Enforcement & (Optional) approval
        approved = self._require_approval_if_needed(action)
        if approved:
            result = action.execute()
            self.auditor.log('operation', action=action.name, result=result)
            return result
        raise Exception('Not approved')

    def narrate(self, record):
        # L5: Audit, notify, narrate
        self.auditor.log('narrate', record=record)
        self.notifier.notify_guardian(f'Action performed: {record}')
        return "Narration complete"

    # Example implementations for internal methods
    def _validate_input(self, input_data):
        return input_data is not None and isinstance(input_data, dict)

    def _analyze_signals(self, input_data):
        # Dummy implementation: risk is 0 unless 'risk' in input_data
        return input_data.get('risk', 0)

    def _require_approval_if_needed(self, action):
        # Dummy implementation: require approval for risky actions
        return getattr(action, 'approved', True)

# --- MOCKS and TESTING ---

class DummyPolicyEngine:
    max_risk = 5

    def evaluate(self, input_data):
        # Allow if risk <= 3
        if input_data.get('risk', 0) <= 3:
            return True, 'Low risk, allowed.'
        return False, 'Risk too high.'

class DummyNotifier:
    def notify_guardian(self, message):
        print(f"Guardian Notification: {message}")

class DummyAuditor:
    def log(self, stage, **kwargs):
        print(f"Audit log [{stage}]:", kwargs)

class DummyAction:
    name = 'do_something'
    approved = True
    def execute(self):
        return "Action was executed!"

# --- TEST CASES ---
if __name__ == '__main__':
    policy_engine = DummyPolicyEngine()
    notifier = DummyNotifier()
    auditor = DummyAuditor()
    agent = OnionAgent(policy_engine, notifier, auditor)

    # Test 1: Normal flow
    print("--- Test 1: Normal Flow ---")
    raw_input = {'data': 123}
    a = agent.observe(raw_input)
    agent.notice(a)
    agent.infer(a)
    result = agent.operate(DummyAction())
    agent.narrate(result)

    # Test 2: High risk input (should notify and fail)
    print("\n--- Test 2: High Risk ---")
    try:
        raw_input = {'data': 99, 'risk': 10}
        a = agent.observe(raw_input)
        agent.notice(a)
        agent.infer(a)
        result = agent.operate(DummyAction())
        agent.narrate(result)
    except Exception as e:
        print("[Handled Exception]", e)

    # Test 3: Invalid input (not a dict)
    print("\n--- Test 3: Invalid Input ---")
    try:
        a = agent.observe("bad input")
    except Exception as e:
        print("[Handled Exception]", e)
