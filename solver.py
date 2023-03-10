import angr
from angr import SimState

# These block addresses were found using Ghidra 10.2.2
BASE_ADDR = 0x400000 # Default angr base addr

WIN_BLOCK_ADDR = BASE_ADDR + 0x1225
EXIT1_BLOCK_ADDR = BASE_ADDR + 0x1212
EXIT2_BLOCK_ADDR = BASE_ADDR + 0x11ec
CONTINUE_BLOCK_ADDR = BASE_ADDR + 0x11a8

wanted_state: SimState = None
def ins_callback(state: SimState):
    global wanted_state
    if state.addr == CONTINUE_BLOCK_ADDR:
        wanted_state = state.copy()

if __name__ == "__main__":
    project = angr.Project("binary")
    entry_state = project.factory.entry_state(args=['./input.txt'])
    sim = project.factory.simgr(entry_state, veritesting=True)

    bp = entry_state.inspect.make_breakpoint(
        'instruction',
        when=angr.state_plugins.inspect.BP_BEFORE,
        action=ins_callback
    )

    # Step until we get to "Continuing"
    while wanted_state is None:
        sim.step()
    wanted_state.inspect.remove_breakpoint('instruction', bp)

    print(f"Ready to explore! State: {hex(wanted_state.addr)}")