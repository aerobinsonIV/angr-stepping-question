import angr

BASE_ADDR = 0x400000 # Default angr base addr

WIN_BLOCK_ADDR = 0x1225
EXIT1_BLOCK_ADDR = 0x1212
EXIT2_BLOCK_ADDR = 0x11ec
CONTINUE_BLOCK_ADDR = 0x11a8

def at_continue(sim: angr.sim_manager.SimulationManager):
    if sim.active[0].addr == CONTINUE_BLOCK_ADDR:
        return True
    else:
        return False

if __name__ == "__main__":
    project = angr.Project("binary")
    entry_state = project.factory.entry_state(args=['./input.txt'])
    sim = project.factory.simgr(entry_state, veritesting=True)

    # Step until we get to "Continuing"
    sim.step(until=at_continue)

    print("Ready to explore!")