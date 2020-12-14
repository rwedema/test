#!/usr/bin/env python3

from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene,Camera

import sys


def molecules():
    ''' Creates molecules and contains other constants '''
    global ETHANOL

    ETHANOL = pdb.PDBMolecule('{}/pdb/ethanol.pdb'.format(SETTINGS.AppLocation), center=True)


def frame(step):
    ''' Renders an Ethanol molecule centered in the scene '''
    ETHANOL = pdb.PDBMolecule('{}/pdb/ethanol.pdb'.format(SETTINGS.AppLocation), center=True)

    camera = Camera('location', [10, 0, 0], 'look_at', [0, 0, 0])
    nframes = eval(SETTINGS.NumberFrames)
    print("aantal frames:",nframes)
    hele_rotatie = 6.283
    print(step)
    # splitsing = ETHANOL.divide([7,8], 'ethanol')
    if step <= (nframes/2):
        y_ass = (1/(nframes/2)) * step
        splitsing = ETHANOL.divide([7,8], 'ethanol', offset=[0, y_ass, 0])
        print(splitsing.center)
        print("de y as",y_ass)
    else:
        # draaien
        y_ass = (1/(nframes / 2)) * 40
        splitsing = ETHANOL.divide([7, 8], 'ethanol', offset=[0, y_ass, 0])
        print(splitsing.center)
        print(splitsing)
        step = step - 40
        rotatie_per_step = (hele_rotatie / nframes) * step

        ETHANOL.rotate_by_step([1, 0, 0], rotatie_per_step, step)
        splitsing.rotate_by_step([1, 0, 0], rotatie_per_step, step)

    # ETHANOL.rotate([1, 0, 0], rotatie_per_step)
    # ETHANOL.show_label(camera=camera, name=True)
    # splitsing.show_label(camera=camera, name=True)

    # Return the Scene object for rendering
    return Scene(camera,
                 objects=[models.default_light] +
                         ETHANOL.povray_molecule + splitsing.povray_molecule,
                 included=['colors.inc'])



def main(args):
    """ Main function performing the rendering """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(38, 44))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))